# ResDaddy – Codebase Analysis

Last updated: 2025-08-08 18:10 (+06:00)

## Summary

- __Purpose__: Full‑stack, AI‑powered resume analysis tool. React SPA frontend uploads a CV + Job Description (JD) to a Flask backend, which calls OpenRouter models and returns a Markdown analysis.
- __Core flow__: `frontend/src/App.js` → POST `FormData` to `backend/app.py:/analyze-cv` → extract CV text (PDF/DOCX) → build prompt (`backend/prompt.md` or `backend/crazyPrompt.md`) → call OpenRouter via `openai` client → return Markdown → `frontend/src/ResultPage.js` renders and can download `.md`.
- __Deploy posture__: Backend has Heroku-style `Procfile` + `runtime.txt`. Frontend has `static.json` for SPA hosting (e.g., heroku-buildpack-static or similar). README provides local setup.

---

## Repository Structure

```
resdaddy/
├─ README.md
├─ LICENSE
├─ .gitignore
├─ package-lock.json              # (root; appears unused)
├─ backend/
│  ├─ app.py                      # Flask app, / and /analyze-cv
│  ├─ models.py                   # OpenRouter model selection
│  ├─ requirements.txt            # Flask, OpenAI client, parsers
│  ├─ .env.example                # OPENROUTER_API_KEY, PORT, FLASK_DEBUG
│  ├─ Procfile                    # web: gunicorn app:app
│  ├─ runtime.txt                 # python-3.9.18
│  ├─ prompt.md                   # conservative analysis
│  ├─ crazyPrompt.md              # fabrication-style prompt (controlled)
│  ├─ DejaVuSans.ttf              # (present; not used in code)
│  └─ (no tests/ subpackage present)
└─ frontend/
   ├─ package.json                # CRA (react-scripts)
   ├─ package-lock.json
   ├─ static.json                 # SPA routes/caching
   ├─ public/
   │  └─ index.html
   └─ src/
      ├─ index.js                 # Router setup
      ├─ App.js                   # Upload form, POST to backend
      ├─ ResultPage.js            # Markdown rendering + download
      ├─ App.css
      └─ ResultPage.css
```

Key docs: `README.md` (good overview, some structure mismatches noted below).

---

## Tech Stack

- __Frontend__: React 18, React Router 6, CRA (`react-scripts`). `react-markdown`, `remark-gfm`. Uses `fetch`; `axios` is listed but not used.
- __Backend__: Python 3.9, Flask + CORS. PDF parsing via `PyPDF2`; DOCX via `python-docx`. OpenRouter API via `openai` client with `api_base` set to `https://openrouter.ai/api/v1`.
- __Deployment__: Heroku-style for backend (`Procfile`, `runtime.txt`). SPA hosting guided by `static.json`.

---

## Backend Details (`backend/`)

- __Entry__: `backend/app.py`
  - `GET /` → `{ "status": "ResDaddy backend running" }` (health).
  - `POST /analyze-cv` (multipart form):
    - Inputs: `cv` (file), `job_desc` (string), `use_crazy_prompt` ("true"/"false").
    - Workflow:
      1) Save upload to temp. 2) Extract text:
         - PDF: `PyPDF2.PdfReader` pages text.
         - DOC/DOCX: `python-docx` (note: `.doc` legacy not actually supported by python-docx).
      3) Load prompt: `backend/crazyPrompt.md` if toggled, else `backend/prompt.md`.
      4) Call OpenRouter via `openai.ChatCompletion.create(...)` with fallback model.
      5) Return JSON: `{ success: true, analysis: "<markdown>" }`.
- __Model config__: `backend/models.py`
  - `DEFAULT_MODEL = "openrouter/horizon-beta"`
  - `FALLBACK_MODEL = "deepseek/deepseek-r1:free"`
- __Env__: `backend/.env.example`
  - `OPENROUTER_API_KEY`, `FLASK_DEBUG`, `PORT`.
- __Runtime__: `Procfile` (gunicorn) and `runtime.txt` (3.9.18).

---

## Frontend Details (`frontend/`)

- __Entry__: `frontend/src/index.js` (Routes `/` → `App`, `/result` → `ResultPage`).
- __App__: `frontend/src/App.js`
  - Form collects CV file, JD text, and a toggle.
  - POST target: `${process.env.REACT_APP_API_URL}/analyze-cv` using `fetch` with `FormData`.
  - On success, navigates to `/result` and passes `analysis` via navigation state.
- __Result__: `frontend/src/ResultPage.js`
  - Renders Markdown using `react-markdown` + `remark-gfm`.
  - Offers a “Download .md” button (downloads client-side as `cv_analysis.md`).
- __Hosting__: `frontend/static.json` for SPA rewrites, cache headers.

---

## API Contract

- __Endpoint__: `POST /analyze-cv`
- __Request__ (multipart/form-data):
  - `cv`: file (.pdf or .docx; `.doc` extension allowed in UI but not actually parsed reliably).
  - `job_desc`: string.
  - `use_crazy_prompt`: "true" | "false".
- __Response__ (application/json):
  - `200`: `{ success: true, analysis: string(markdown) }`.
  - `4xx/5xx`: `{ error: string }` with reason (missing inputs, unsupported file type, extraction or API error, etc.).

---

## Prompts

- `backend/prompt.md`: Conservative rubric-based analysis and rewriting guidance, with explicit output format.
- `backend/crazyPrompt.md`: Fabrication-oriented but constrained; invents role titles and bullets to align with JD while preserving real companies/dates; ATS-friendly output.

---

## Build & Run (Local)

- __Backend__ (`backend/`):
  1) Create `.env` from `.env.example` and set `OPENROUTER_API_KEY`.
  2) `pip install -r requirements.txt`
  3) `python app.py` → `http://localhost:5000`

- __Frontend__ (`frontend/`):
  1) Create `.env` with:
     ```env
     REACT_APP_API_URL=http://localhost:5000
     ```
  2) `npm install`
  3) `npm start` → `http://localhost:3000`

---

## Notable Observations & Risks

- __Frontend API base required__
  - `App.js` depends on `process.env.REACT_APP_API_URL`; without `frontend/.env`, calls become `undefined/analyze-cv`.
  - Add `frontend/.env.example` and/or a fallback in code for dev.

- __`.doc` support mismatch__
  - UI accepts `.doc`, but backend uses `python-docx` which does not parse legacy `.doc` reliably → errors.
  - Either remove `.doc` from file input accept list or add a `.doc` parsing path (e.g., `textract`, `antiword`, `libreoffice` conversion).

- __OpenAI client API version risk__
  - Code uses legacy `openai.ChatCompletion.create(...)`. `backend/requirements.txt` has unpinned `openai`.
  - Options:
    - Pin `openai<1.0.0`, or
    - Upgrade code to v1 client style (`OpenAI` client) to be future-proof.

- __Token limits__
  - `max_tokens=10000` may exceed some OpenRouter model caps → failures. Consider safer default (e.g., 1500–3000) and/or input truncation.

- __CORS in prod__
  - `CORS(app)` currently wide open. Restrict origins in production via env (keep open in dev).

- __Unused/extra deps & files__
  - Frontend lists `axios` but uses `fetch`.
  - Backend includes `fpdf` and `DejaVuSans.ttf` but does not generate PDFs currently.
  - Root `package-lock.json` without root `package.json` looks stale.

- __Docs mismatch__
  - README shows a deeper backend package structure (`app/`, `routes/`, `services/`, `tests/`) not present. Current backend is flat. Align README or refactor.
  - README mentions `FLASK_ENV`; env example uses `FLASK_DEBUG`. Standardize.

- __Validation & logging__
  - No explicit file size/type caps beyond extension. Add size limit and MIME checks.
  - Heavy `print` usage. Prefer `logging` with levels; return consistent error shapes.

- __Security__
  - API key resides server-side only (good). Ensure no logs leak prompts or PII in production.

---

## Recommended Actions

1) __Frontend config__
   - Add `frontend/.env.example` with `REACT_APP_API_URL=`.
   - In `App.js`, add a dev fallback to `http://localhost:5000` if env var missing.
   - Remove `.doc` from `accept` attribute unless backend gains true `.doc` support.
   - Remove `axios` (or refactor to use it consistently).

2) __Backend stability__
   - Pin `openai<1.0.0` in `requirements.txt` or migrate to v1 client API.
   - Reduce `max_tokens` and add defensive truncation for long inputs.
   - Restrict CORS via env (e.g., `ALLOWED_ORIGINS`).
   - Validate uploads (size, MIME) and handle `.doc` explicitly.
   - Replace `print` with `logging` and standardize error responses.
   - Remove unused `fpdf`/font or implement a PDF export endpoint if desired.

3) __Docs & hygiene__
   - Sync README structure with current code or refactor to match the documented structure.
   - Remove root `package-lock.json` if unused to avoid confusion.

---

## Quick PR Plan (Optional)

- PR 1: Frontend dev UX
  - Add `frontend/.env.example`; fallback base URL in `App.js`; remove `.doc` from `accept`; remove `axios` if unused.
- PR 2: Backend safety & compatibility
  - Pin `openai<1.0.0` (or migrate to v1 client), set `max_tokens` to safer default, add upload validations, introduce env-based CORS.
- PR 3: Docs & cleanup
  - Update README, add `frontend/.env.example`, remove root `package-lock.json`, remove unused `fpdf`/font or add PDF export.

---

## Appendix: Key Files

- Frontend: `frontend/src/index.js`, `frontend/src/App.js`, `frontend/src/ResultPage.js`, `frontend/static.json`, `frontend/package.json`
- Backend: `backend/app.py`, `backend/models.py`, `backend/requirements.txt`, `backend/.env.example`, `backend/Procfile`, `backend/runtime.txt`, `backend/prompt.md`, `backend/crazyPrompt.md`
