# Phase 7 — Project Documentation

## Project Summary
LegalEase is an AI-assisted legal document generator based on the supplied
SmartBridge project specification.

## Technology Stack
- Python
- FastAPI
- Streamlit
- Google Gemini SDK
- python-docx
- fpdf2
- Pillow
- requests
- python-dotenv
- pytest

## Installation

```bash
python -m venv .venv
pip install -r requirements.txt
```

Configure `.env`, then run:

```bash
uvicorn main:app --reload
streamlit run app.py
```

## API

### POST `/generate`

Example request:

```json
{
  "document_type": "Freelance Work Contract",
  "parties": "Jane Doe (Provider), TechNova Inc. (Client)",
  "terms": "Payment within 30 days; Confidentiality required",
  "dates": "September 28, 2026",
  "jurisdiction": "Not specified",
  "additional_instructions": ""
}
```

### Response
```json
{
  "success": true,
  "document": "..."
}
```

## Security Notes
- API keys belong in `.env`.
- `.env` is ignored by Git.
- Do not commit credentials.
- Avoid storing unnecessary sensitive user information.

## Legal Notice
This project generates AI-assisted drafts for educational and drafting
purposes. It is not a substitute for professional legal advice.
