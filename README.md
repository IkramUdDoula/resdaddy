# ResDaddyOld Project

This is a full-stack web application with a React frontend and a Python (Flask) backend.

## Tech Stack

*   **Frontend:** React.js
*   **Backend:** Python with Flask

## Project Structure

```
ResDaddyOld-main/
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── App.js
│   │   ├── index.js
│   │   └── ... (other React components)
│   ├── package.json
│   └── ...
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   └── ...
├── .gitignore
└── README.md
```

## Getting Started

### Prerequisites

*   Node.js and npm installed
*   Python and pip installed

### Configuration

To use the OpenAI integration, you need to add your API key.

1.  In the `backend` directory, create a file named `.env`.
2.  Add the following line to the `.env` file, replacing `your_api_key_here` with your actual OpenAI API key:

    ```
    OPENAI_API_KEY='your_api_key_here'
    ```

### Installation & Running

**1. Backend (Flask)**

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
