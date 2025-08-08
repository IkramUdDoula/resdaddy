# ResDaddy - AI-Powered Resume Analysis Tool

ResDaddy is a comprehensive resume analysis platform that leverages AI to help job seekers improve their resumes. The application provides detailed feedback, suggestions, and optimization tips to make your resume stand out to potential employers.

## ✨ Features

- **AI-Powered Analysis**: Get instant feedback on your resume content
- **Multiple Format Support**: Upload resumes in PDF or DOCX formats (legacy .doc not supported)
- **ATS Optimization**: Improve your resume's compatibility with Applicant Tracking Systems
- **Detailed Reports**: Receive comprehensive analysis and improvement suggestions
- **User-Friendly Interface**: Clean, intuitive design for seamless user experience

## 🛠 Tech Stack

### Frontend
- React.js (Create React App)
- React Router
- react-markdown + remark-gfm
- fetch for API calls

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
- Python (3.9 or later) and pip
- Git
- OpenRouter API Key ([Get it here](https://openrouter.ai/))

### Project Structure

```
ResDaddy/
├── frontend/               # React frontend (CRA)
│   ├── public/             # Static assets
│   ├── src/                # Source code
│   │   ├── App.js          # Main component
│   │   ├── ResultPage.js   # Results view
│   │   └── index.js        # Entry point / routing
│   ├── package.json        # Frontend dependencies
│   ├── static.json         # SPA hosting config
│   ├── Dockerfile          # Multi-stage build and Nginx runtime
│   └── nginx/
│       └── default.conf    # Nginx config (SPA + /api proxy)
│
├── backend/                # Flask backend
│   ├── app.py              # Application entry point
│   ├── models.py           # OpenRouter model selection
│   ├── requirements.txt    # Python dependencies
│   ├── .env.example        # Environment variables template
│   ├── Procfile            # Heroku process types
│   ├── runtime.txt         # Python runtime
│   ├── prompt.md           # Analysis prompt
│   ├── crazyPrompt.md      # Fabrication prompt (optional)
│   └── Dockerfile          # Gunicorn-based production image
│
├── docker-compose.yml      # Orchestration (Option B: Nginx proxy)
├── .gitignore
├── LICENSE
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
   Edit `.env` and set:
   ```
   OPENROUTER_API_KEY=your_api_key_here
   FLASK_DEBUG=true
   PORT=5000
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
   The frontend will open automatically at `http://localhost:3000`.

   Notes:
   - The app now uses a relative API path (`/api`). For local development, CRA is configured with a proxy in `frontend/src/setupProxy.js` that forwards `/api` to `http://localhost:5000`.
   - Ensure the backend is running on port 5000 before starting the frontend.

## 🚀 Deployment

### Docker (Option B: Nginx reverse proxy)

This setup serves the React SPA via Nginx and proxies `/api` to the Flask backend. A single port (80) is exposed.

1. Create a backend environment file:
   ```bash
   cp backend/.env.example backend/.env
   ```
   Then edit `backend/.env` and set:
   ```dotenv
   OPENROUTER_API_KEY=your_api_key_here
   FLASK_DEBUG=false
   PORT=5000
   ```

2. Build and run with Docker Compose:
   ```bash
   docker compose up -d --build
   ```

3. Open the app:
   - http://localhost/

4. Stop the stack:
   ```bash
   docker compose down
   ```

The `frontend` container listens on port 80 and proxies `/api` to the `backend` service (port 5000) within the Docker network.

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
- `OPENROUTER_API_KEY`: Required for AI analysis (server-side)
- `FLASK_DEBUG`: `true` for development, `false` for production (default: `false`)
- `PORT`: Server port (default: `5000`)

### Frontend
- None required in the default setup. The app uses a relative path (`/api`) and, in development, CRA proxies to `http://localhost:5000` via `frontend/src/setupProxy.js`.
  - For legacy setups, you may still use `REACT_APP_API_URL`, but it's not needed with the Nginx proxy.

## 🐛 Troubleshooting

- **Port conflicts**: Change the port via `PORT` in backend `.env` or adjust frontend dev server port
- **Missing dependencies**: Run `npm install` or `pip install -r requirements.txt`
- **API connection issues**: Verify your OpenRouter API key in `backend/.env`
- **Frontend API base URL**: Not needed in the default setup. Ensure the backend runs on `http://localhost:5000` in dev (CRA proxy) or use Docker Option B (single origin).
- **Legacy .doc uploads**: `.doc` is not reliably supported; use `.pdf` or `.docx`
- **Model/client errors**: If you see OpenAI client errors, pin `openai<1.0.0` in `backend/requirements.txt` or update the code to the v1 client API. Reduce `max_tokens` if model limits are exceeded.
 - **Payload too large (413)**: If CV uploads are blocked in Docker, Nginx may need a higher limit. Adjust `client_max_body_size` in `frontend/nginx/default.conf` and rebuild.

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the GNU GENERAL PUBLIC LICENSE - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- OpenRouter for their powerful AI API
- The open-source community for their valuable contributions
