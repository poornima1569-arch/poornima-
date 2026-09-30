# Phase 8 — Project Demonstration

## Demo Video Checklist

The required demo should include:

1. Project name: LegalEase.
2. Purpose of the project.
3. Benefits/use cases.
4. Project execution and working process.
5. Final output.

## Suggested 5–7 Minute Demo Script

### 0:00–0:30 — Introduction
“Hello everyone. Our project is LegalEase, an AI-powered legal document
generator. It helps users create structured, editable legal-document drafts
from simple inputs.”

### 0:30–1:15 — Purpose and Benefits
Explain that the application accepts document type, parties, terms and
effective date, then produces an editable draft and multiple download formats.

### 1:15–2:00 — Architecture
Show:
Streamlit → FastAPI → Gemini → formatted output.

### 2:00–3:15 — Live Input
Select “Freelance Work Contract”.
Enter example parties and terms.
Enter an effective date.
Click Generate Document.

### 3:15–4:15 — Preview and Editing
Show the generated text.
Edit one clause.
Explain that the preview is editable.

### 4:15–5:15 — Downloads
Download:
- TXT
- DOCX
- PDF

Open at least the DOCX or PDF and show formatting.

### 5:15–6:00 — Backend
Open FastAPI `/docs` and show `/generate`.
Open `/health`.

### 6:00–6:30 — Closing
Show the final output and state the legal-review notice.

## Demo Example

Document Type:
Freelance Work Contract

Parties:
Jane Doe (Service Provider), TechNova Inc. (Client)

Terms:
Payment within 30 days; Provider delivers work by agreed deadline;
Confidentiality must be maintained; Either party may terminate with 15 days notice

Effective Date:
September 28, 2026

## Google Drive Submission
Upload the recorded video and set sharing to:
“Anyone with the link can view.”

Do not include private API keys or personal credentials in the recording.
