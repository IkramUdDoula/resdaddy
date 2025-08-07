# ResDaddy - AI-Powered Resume Analysis Tool

ResDaddy is a comprehensive resume analysis platform that leverages AI to help job seekers improve their resumes. The application provides detailed feedback, suggestions, and optimization tips to make your resume stand out to potential employers.

## ✨ Features

- **AI-Powered Analysis**: Get instant feedback on your resume content
- **Multiple Format Support**: Upload resumes in PDF or DOCX formats
- **ATS Optimization**: Improve your resume's compatibility with Applicant Tracking Systems
- **Detailed Reports**: Receive comprehensive analysis and improvement suggestions
- **User-Friendly Interface**: Clean, intuitive design for seamless user experience

## 🛠 Tech Stack

### Frontend
- React.js
- React Router
- Styled Components
- Axios for API calls

### Backend
- Python with Flask
- OpenRouter API for AI capabilities
- RESTful API architecture

### Development Tools
- Git for version control
- npm / yarn for package management
- pip for Python dependencies

## 🚀 Getting Started

### Prerequisites

- Node.js (v14 or later) and npm (v6 or later)
- Python (3.8 or later) and pip
- Git
- OpenRouter API Key ([Get it here](https://openrouter.ai/))

### Project Structure

```
ResDaddy/
├── frontend/               # React frontend
│   ├── public/             # Static assets
│   ├── src/                # Source code
│   │   ├── components/     # Reusable UI components
│   │   ├── assets/         # Images, fonts, etc.
│   │   ├── services/       # API services
│   │   ├── App.js          # Main component
│   │   └── index.js        # Entry point
│   └── package.json        # Frontend dependencies
│
├── backend/                # Flask backend
│   ├── app/               # Application package
│   │   ├── __init__.py    # App factory
│   │   ├── routes/        # API routes
│   │   └── services/      # Business logic
│   ├── tests/             # Test files
│   ├── app.py             # Application entry point
│   ├── requirements.txt   # Python dependencies
│   └── .env.example       # Environment variables template
│
├── .gitignore
└── README.md
```

## 🛠 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/ResDaddy.git
cd ResDaddy
```

### 2. Backend Setup

1. **Set up virtual environment and install dependencies:**
   ```bash
   cd backend
   python -m venv venv
   
   # On Windows
   .\venv\Scripts\activate
   # On macOS/Linux
   # source venv/bin/activate
   
   pip install -r requirements.txt
   ```

2. **Configure environment variables:**
   ```bash
   cp .env.example .env
   ```
   Edit `.env` and add your OpenRouter API key:
   ```
   OPENROUTER_API_KEY='your_api_key_here'
   FLASK_ENV=development
   ```

3. **Run the backend server:**
   ```bash
   python app.py
   ```
   The API will be available at `http://localhost:5000`

### 3. Frontend Setup

1. **Install dependencies and start the development server:**
   ```bash
   cd ../frontend
   npm install
   npm start
   ```
   The frontend will open automatically at `http://localhost:3000`

## 🚀 Deployment

### Backend (Production)

```bash
# In the backend directory
gunicorn --bind 0.0.0.0:5000 app:app
```

### Frontend (Production)

```bash
# In the frontend directory
npm run build
```
Serve the `build` directory using your preferred static file server.

## 🔧 Environment Variables

### Backend
- `OPENROUTER_API_KEY`: Required for AI analysis
- `FLASK_ENV`: Set to 'production' or 'development'
- `PORT`: Server port (default: 5000)

## 🐛 Troubleshooting

- **Port conflicts**: Change the port in `app.py` (backend) or `package.json` (frontend)
- **Missing dependencies**: Run `npm install` or `pip install -r requirements.txt`
- **API connection issues**: Verify your OpenRouter API key in `.env`

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- OpenRouter for their powerful AI API
- The open-source community for their valuable contributions
