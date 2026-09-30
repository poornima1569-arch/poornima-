# Phase 3 — Project Design

## Architecture

```text
+----------------------+
|   Streamlit Frontend |
| Inputs / Preview /   |
| Editing / Downloads  |
+----------+-----------+
           |
           | HTTP POST /generate
           v
+----------------------+
|     FastAPI API      |
| Pydantic validation  |
| routes.py            |
+----------+-----------+
           |
           v
+----------------------+
| GeminiDocumentGenerator|
| Prompt construction  |
| Gemini generation    |
+----------+-----------+
           |
           v
+----------------------+
| Document Formatter   |
| TXT / DOCX / PDF     |
+----------------------+
```

## Main Components

### Frontend
`app.py`
- Input controls
- Generate button
- Editable text area
- HTML preview
- Download buttons

### Backend
`main.py`
- Initializes FastAPI
- Root and health endpoints
- Includes API router

`routes.py`
- Defines `DocumentRequest`
- Implements `/generate`
- Calls the AI generator

### AI Core
`ai_core/gemini_generator.py`
- Loads environment variables
- Configures Gemini
- Builds structured prompt
- Provides local fallback demo mode

### Formatting
`utils/document_formatter.py`
- Text sanitization
- TXT bytes
- DOCX generation
- PDF generation
- Headers/footers and legal-document formatting

## Data Flow

1. User enters document details.
2. Streamlit sends JSON to FastAPI.
3. Pydantic validates the request.
4. Gemini generator builds the prompt.
5. Gemini returns generated text when configured.
6. The frontend displays editable text.
7. User downloads TXT/DOCX/PDF.

## UI Design
The interface uses a two-column layout:
- Left: input form.
- Right: generated/editable document.

A dark preview card provides a document-style reading area.
