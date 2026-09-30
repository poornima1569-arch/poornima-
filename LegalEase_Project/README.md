# LegalEase — AI-Powered Legal Document Generator

LegalEase is an educational project based on the supplied SmartBridge project
document. It uses **Streamlit** for the frontend, **FastAPI** for the backend,
and **Gemini** for AI-assisted document generation. It supports editable
previews and downloads as **TXT, DOCX and PDF**.

The supplied project document specifically describes Gemini 1.5 Pro,
FastAPI, Streamlit, `python-docx`, `fpdf`, Pillow, requests and
python-dotenv. This implementation follows that requested architecture.

## Features

- Employment contracts
- NDAs
- Lease agreements
- Freelance/service agreements
- Custom legal document drafts
- Parties, terms and effective-date inputs
- Optional jurisdiction and instructions
- AI generation through Gemini
- Local demo mode when no Gemini API key is configured
- Editable generated document
- TXT export
- DOCX export with Times New Roman formatting and footer
- PDF export with header/footer
- FastAPI `/generate` API
- Health endpoint
- Automated API tests

## Project Structure

```text
LegalEase_Project/
├── app.py
├── main.py
├── routes.py
├── requirements.txt
├── .env.example
├── .gitignore
├── pytest.ini
├── README.md
├── ai_core/
│   ├── __init__.py
│   └── gemini_generator.py
├── utils/
│   ├── __init__.py
│   └── document_formatter.py
├── tests/
│   └── test_api.py
├── phases/
│   ├── 01_brainstorming_ideation.md
│   ├── 02_requirement_analysis.md
│   ├── 03_project_design.md
│   ├── 04_project_planning.md
│   ├── 05_project_development.md
│   ├── 06_project_testing.md
│   ├── 07_project_documentation.md
│   └── 08_project_demonstration.md
└── assets/
    └── README.md
```

## Setup

### 1. Create environment

Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

Windows CMD:

```cmd
python -m venv .venv
.venv\Scripts\activate
```

### 2. Install packages

```bash
pip install -r requirements.txt
```

### 3. Configure Gemini

Copy `.env.example` to `.env`.

```text
GEMINI_API_KEY=your_key
GEMINI_MODEL=gemini-1.5-pro
BACKEND_URL=http://127.0.0.1:8000
```

Do not upload `.env` to GitHub.

### 4. Start backend

```bash
uvicorn main:app --reload
```

Backend:
- http://127.0.0.1:8000
- Swagger UI: http://127.0.0.1:8000/docs

### 5. Start frontend

Open a second terminal:

```bash
streamlit run app.py
```

Open the Streamlit URL shown in the terminal.

## Demo without an API key

The app contains a local fallback generator. This lets the team demonstrate
the interface, editing and downloads even before a Gemini API key is added.
For an actual Gemini-backed generation demonstration, configure the API key.

## Test

```bash
pytest
```

## GitHub submission

Create a **public** GitHub repository and upload this project. Keep the
`phases/` directory because it contains the eight required submission phases.

Do not upload:
- `.env`
- API keys
- passwords
- private credentials

## Legal and educational notice

LegalEase is an educational AI-assisted drafting project. Generated text can
contain errors and should be reviewed by a qualified legal professional before
real-world use.
