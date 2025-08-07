from dotenv import load_dotenv
load_dotenv()

from flask import Flask, request, send_file, jsonify
from flask_cors import CORS
import os
from models import DEFAULT_MODEL, FALLBACK_MODEL

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return jsonify({'status': 'ResDaddy backend running'})

@app.route('/analyze-cv', methods=['POST'])
def analyze_cv():
    import tempfile
    import openai
    from werkzeug.utils import secure_filename
    from PyPDF2 import PdfReader
    from docx import Document as DocxDocument
    from fpdf import FPDF
    import traceback

    print('Received request to /analyze-cv')

    # --- Config ---
    OPENROUTER_API_KEY = os.environ.get('OPENROUTER_API_KEY')


    # --- Validate request ---
    if 'cv' not in request.files or 'job_desc' not in request.form:
        print('Missing CV file or job description')
        return jsonify({'error': 'Missing CV file or job description'}), 400

    cv_file = request.files['cv']
    job_desc = request.form['job_desc']
    use_crazy_prompt = request.form.get('use_crazy_prompt') == 'true'

    if use_crazy_prompt:
        PROMPT_PATH = os.path.join(os.path.dirname(__file__), 'crazyPrompt.md')
    else:
        PROMPT_PATH = os.path.join(os.path.dirname(__file__), 'prompt.md')
    filename = secure_filename(cv_file.filename)
    ext = os.path.splitext(filename)[1].lower()

    print(f'Uploaded file: {filename}, extension: {ext}')

    # --- Save uploaded file to temp ---
    with tempfile.NamedTemporaryFile(delete=False, suffix=ext) as tmp_file:
        cv_file.save(tmp_file.name)
        cv_path = tmp_file.name

    # --- Extract text from CV ---
    try:
        if ext == '.pdf':
            reader = PdfReader(cv_path)
            cv_text = '\n'.join([page.extract_text() or '' for page in reader.pages])
        elif ext in ['.doc', '.docx']:
            doc = DocxDocument(cv_path)
            cv_text = '\n'.join([p.text for p in doc.paragraphs])
        else:
            os.unlink(cv_path)
            print('Unsupported file type')
            return jsonify({'error': 'Unsupported file type'}), 400
    except Exception as e:
        os.unlink(cv_path)
        print('Failed to extract text:', str(e))
        traceback.print_exc()
        return jsonify({'error': f'Failed to extract text: {str(e)}'}), 500

    os.unlink(cv_path)
    print('Extracted CV text, length:', len(cv_text))

    # --- Prepare OpenAI prompt ---
    try:
        with open(PROMPT_PATH, 'r', encoding='utf-8') as f:
            prompt_template = f.read()
    except Exception as e:
        print('Prompt template not found:', str(e))
        traceback.print_exc()
        return jsonify({'error': f'Prompt template not found: {str(e)}'}), 500

    full_prompt = f"""{prompt_template}\n\nCV:\n{cv_text}\n\nJob Description:\n{job_desc}"""
    print('Prepared prompt for OpenAI, length:', len(full_prompt))

    # --- Query OpenRouter ---
    # --- Query OpenRouter ---
    openai.api_base = "https://openrouter.ai/api/v1"
    openai.api_key = OPENROUTER_API_KEY
    try:
        print(f'Calling OpenRouter API with model: {DEFAULT_MODEL}...')
        response = openai.ChatCompletion.create(
            model=DEFAULT_MODEL,
            messages=[{"role": "user", "content": full_prompt}],
            max_tokens=10000,
            temperature=0.7
        )
        ai_output = response['choices'][0]['message']['content']
        print(f'Received response from {DEFAULT_MODEL}, length:', len(ai_output))
    except Exception as e:
        print(f'API call with {DEFAULT_MODEL} failed: {str(e)}')
        print(f'Trying fallback model: {FALLBACK_MODEL}...')
        try:
            response = openai.ChatCompletion.create(
                model=FALLBACK_MODEL,
                messages=[{"role": "user", "content": full_prompt}],
                max_tokens=10000,
                temperature=0.7
            )
            ai_output = response['choices'][0]['message']['content']
            print(f'Received response from {FALLBACK_MODEL}, length:', len(ai_output))
        except Exception as fallback_e:
            print(f'Fallback model {FALLBACK_MODEL} also failed: {str(fallback_e)}')
            traceback.print_exc()
            return jsonify({'error': f'API error with both default and fallback models: {str(fallback_e)}'}), 500

    # --- Return AI output as JSON ---
    try:
        print('Returning AI output to frontend...')
        return jsonify({
            'success': True,
            'analysis': ai_output
        })
    except Exception as e:
        print('Error returning response:', str(e))
        traceback.print_exc()
        return jsonify({'error': f'Response error: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
