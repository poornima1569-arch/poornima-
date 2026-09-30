import os
from dotenv import load_dotenv

load_dotenv()

try:
    import google.generativeai as genai
except ImportError:
    genai = None


class GeminiDocumentGenerator:
    """
    Gemini-backed legal document generator.

    The project document specifies Gemini 1.5 Pro. The code keeps that model
    as the default requested model. If no API key is configured, a safe local
    demo document is returned so the UI can still be demonstrated.
    """

    def __init__(self):
        self.api_key = os.getenv("GEMINI_API_KEY", "").strip()
        self.model_name = os.getenv("GEMINI_MODEL", "gemini-1.5-pro")

        if self.api_key and genai:
            genai.configure(api_key=self.api_key)
            self.model = genai.GenerativeModel(self.model_name)
        else:
            self.model = None

    def generate_document(
        self,
        document_type: str,
        parties: str,
        terms: str,
        dates: str,
        jurisdiction: str = "Not specified",
        additional_instructions: str = "",
    ) -> str:
        if self.model:
            prompt = self._build_prompt(
                document_type, parties, terms, dates,
                jurisdiction, additional_instructions
            )
            response = self.model.generate_content(prompt)
            text = getattr(response, "text", None)
            if text:
                return text.strip()

        return self._demo_document(
            document_type, parties, terms, dates,
            jurisdiction, additional_instructions
        )

    def _build_prompt(
        self, document_type, parties, terms, dates,
        jurisdiction, additional_instructions
    ):
        return f"""
You are the document-generation engine for LegalEase.

Create a structured draft of a {document_type}.
This is a drafting aid, not legal advice. Do not claim that the document is
legally valid in every jurisdiction. Use placeholders when information is
missing.

PARTIES:
{parties}

EFFECTIVE DATE:
{dates}

JURISDICTION:
{jurisdiction}

TERMS AND CONDITIONS:
{terms}

ADDITIONAL INSTRUCTIONS:
{additional_instructions or "None"}

Requirements:
1. Use a professional legal-document structure.
2. Include title, parties, effective date, recitals/background when useful,
   definitions where useful, numbered clauses, obligations, payment/term/
   termination/confidentiality clauses when relevant, and signature blocks.
3. Preserve the user's supplied facts and terms.
4. Do not invent personal identifiers, addresses, amounts, dates, or legal
   authorities.
5. End with a short "Important Notice" stating that the draft should be
   reviewed by a qualified legal professional before use.
6. Return plain text with clear headings.
"""

    def _demo_document(
        self, document_type, parties, terms, dates,
        jurisdiction, additional_instructions
    ):
        term_items = [x.strip() for x in terms.split(";") if x.strip()]
        term_lines = "\n".join(
            f"{i}. {item}" for i, item in enumerate(term_items, 1)
        ) or "1. No specific terms supplied."

        return f"""{document_type.upper()}

Effective Date: {dates}
Jurisdiction: {jurisdiction}

PARTIES
{parties}

PURPOSE
This draft has been prepared from the information entered into LegalEase.
It is intended as an editable starting point for review and customization.

TERMS AND CONDITIONS
{term_lines}

GENERAL PROVISIONS
1. Entire Agreement. This document records the terms supplied for this draft.
2. Amendments. Any amendment should be recorded in writing and approved by
   the relevant parties.
3. Notices. Notices should be delivered using contact details agreed by the
   parties.
4. Governing Law. The parties should specify the governing law applicable to
   their agreement.
5. Severability. If a provision is found unenforceable, the remaining
   provisions should continue to the extent permitted by applicable law.

ADDITIONAL INSTRUCTIONS
{additional_instructions or "None"}

SIGNATURES

Party 1: ______________________________
Name: _________________________________
Date: __________________________________

Party 2: ______________________________
Name: _________________________________
Date: __________________________________

IMPORTANT NOTICE
This LegalEase output is an AI-assisted draft and is not legal advice.
Review the document with a qualified legal professional before signing or
using it.
"""
