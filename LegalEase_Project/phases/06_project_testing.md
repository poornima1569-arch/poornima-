# Phase 6 — Project Testing

## Test Environment
- Python 3.10+
- FastAPI
- Streamlit
- Gemini-compatible configuration
- Modern desktop browser

## Automated Tests

Run:

```bash
pytest
```

Current tests verify:
1. Root endpoint.
2. Health endpoint.
3. Document generation route in local fallback mode.

## Manual Test Cases

| ID | Test | Expected Result |
|---|---|---|
| TC01 | Open frontend | UI loads |
| TC02 | Submit blank required fields | Validation message |
| TC03 | Enter contract details | Request is sent |
| TC04 | Generate without API key | Demo document appears |
| TC05 | Generate with Gemini key | Gemini output appears |
| TC06 | Edit generated text | Changes remain in editor |
| TC07 | Download TXT | Valid TXT file |
| TC08 | Download DOCX | Word file opens |
| TC09 | Download PDF | PDF opens and is formatted |
| TC10 | Open `/docs` | FastAPI Swagger UI appears |
| TC11 | Open `/health` | Healthy response |
| TC12 | Invalid API request | FastAPI validation response |

## Acceptance Criteria
- End-to-end generation works.
- Required fields are validated.
- Output is editable.
- All three download formats work.
- Secrets are not hard-coded.
- Backend and frontend run separately.
