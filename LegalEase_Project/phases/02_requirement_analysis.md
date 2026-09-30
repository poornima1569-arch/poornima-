# Phase 2 — Requirement Analysis

## Functional Requirements

| ID | Requirement | Priority |
|---|---|---|
| FR1 | Accept document type | High |
| FR2 | Accept parties | High |
| FR3 | Accept terms and conditions | High |
| FR4 | Accept effective date | High |
| FR5 | Generate document through backend | High |
| FR6 | Display editable preview | High |
| FR7 | Export TXT | High |
| FR8 | Export DOCX | High |
| FR9 | Export PDF | High |
| FR10 | Provide API health endpoint | Medium |
| FR11 | Support optional jurisdiction | Medium |
| FR12 | Support additional instructions | Medium |

## Non-Functional Requirements

- Usable browser interface.
- Clear validation for required inputs.
- API-based separation between frontend and AI logic.
- Environment-variable based secret management.
- Reasonable document formatting.
- Maintainable modular code.
- Testable API endpoints.

## Inputs
- Document type
- Parties
- Terms
- Effective date
- Optional jurisdiction
- Optional additional instructions

## Outputs
- Generated legal-document text
- TXT file
- DOCX file
- PDF file

## Assumptions
The project document specifies Gemini 1.5 Pro as the selected model. The
implementation preserves that model name as the default configuration.

## Risks
- AI-generated content may contain inaccuracies.
- Gemini availability/API changes may require configuration updates.
- Legal requirements differ by jurisdiction.
- Sensitive user data should not be unnecessarily stored.
