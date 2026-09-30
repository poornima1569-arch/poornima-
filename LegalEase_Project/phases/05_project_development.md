# Phase 5 — Project Development

## Implemented Files

- `main.py`
- `routes.py`
- `app.py`
- `ai_core/gemini_generator.py`
- `utils/document_formatter.py`
- `requirements.txt`
- `tests/test_api.py`

## Backend Development
FastAPI exposes:
- `GET /`
- `GET /health`
- `POST /generate`

`DocumentRequest` validates:
- document type
- parties
- terms
- date
- optional jurisdiction
- optional instructions

## AI Development
The generator:
1. Loads `GEMINI_API_KEY`.
2. Uses `GEMINI_MODEL`, defaulting to the model specified in the supplied
   project document.
3. Creates a structured prompt.
4. Requests a professional draft.
5. Falls back to a local demonstration document if the API is not configured.

## Frontend Development
Streamlit provides:
- Document type selector
- Parties field
- Terms field
- Effective date
- Jurisdiction
- Additional instructions
- Generate button
- Editable output
- Styled preview
- TXT/DOCX/PDF downloads

## Export Development
DOCX:
- Times New Roman
- Centered title
- Footer
- Structured paragraphs

PDF:
- LegalEase header
- Document title
- Footer
- Bold section/numbered lines

TXT:
- Sanitized plain text
