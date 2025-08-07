# ResDaddy - Resume Analysis Tool

ResDaddy is a full-stack web application that helps analyze and improve resumes using AI. It features a React frontend and a Python (Flask) backend with AI-powered analysis capabilities.

## Tech Stack

* **Frontend:** React.js, React Router
* **Backend:** Python with Flask
* **AI Integration:** OpenRouter API
* **Document Processing:** PDF, DOCX support

## Prerequisites

Before you begin, ensure you have the following installed:

* **Node.js** (v14 or later) and **npm** (v6 or later)
* **Python** (3.8 or later) and **pip** (Python package manager)
* **Git** (for cloning the repository)
* **OpenRouter API Key** (get it from [OpenRouter](https://openrouter.ai/))

## Project Structure

```
ResDaddy/
├── frontend/               # React frontend application
│   ├── public/             # Static files
│   ├── src/                # React source code
│   │   ├── components/     # Reusable components
│   │   ├── App.js          # Main application component
│   │   ├── index.js        # Entry point
│   │   └── ...
│   ├── package.json        # Frontend dependencies
│   └── ...
├── backend/                # Flask backend
│   ├── app.py             # Main application file
│   ├── requirements.txt    # Python dependencies
│   ├── .env.example       # Example environment variables
│   └── ...
├── .gitignore
└── README.md
```

## Local Development Setup

### 1. Clone the Repository

```bash
git clone <repository-url>
cd ResDaddy
```

### 2. Backend Setup

1. **Navigate to the backend directory and create a virtual environment:**
   ```bash
   cd backend
   python -m venv venv
   ```

2. **Activate the virtual environment:**
   - On Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

3. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   - Copy the example environment file:
     ```bash
     copy .env.example .env
     ```
   - Edit the `.env` file and add your OpenRouter API key:
     ```
     OPENROUTER_API_KEY='your_openrouter_api_key_here'
     ```

5. **Run the Flask development server:**
   ```bash
   python app.py
   ```
   The backend will be available at `http://localhost:5000`

### 3. Frontend Setup

1. **Navigate to the frontend directory:**
   ```bash
   cd ../frontend
   ```

2. **Install Node.js dependencies:**
   ```bash
   npm install
   ```

3. **Start the development server:**
   ```bash
   npm start
   ```
   The frontend will be available at `http://localhost:3000`

## Running in Production

### Backend
For production, it's recommended to use a production WSGI server like Gunicorn:

```bash
# In the backend directory
gunicorn --bind 0.0.0.0:5000 app:app
```

### Frontend
Build the optimized production bundle:

```bash
# In the frontend directory
npm run build
```

## Environment Variables

### Backend
- `OPENROUTER_API_KEY`: Your OpenRouter API key (required)
- `FLASK_ENV`: Set to 'development' or 'production' (optional)

## Troubleshooting

- **Port already in use**: If you encounter port conflicts, you can change the port in `app.py` for the backend or in `frontend/package.json` for the frontend.
- **Missing dependencies**: Ensure all dependencies are installed by following the setup steps above.
- **API errors**: Verify your OpenRouter API key is correctly set in the `.env` file.

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

```bash
# Navigate to the backend directory
cd backend

# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

# Install dependencies
pip install -r requirements.txt

# Run the Flask server
flask run
```

**2. Frontend (React)**

```bash
# Navigate to the frontend directory in a new terminal
cd frontend

# Install dependencies
npm install

# Run the React development server
npm start
```
