from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from ai_core.gemini_generator import GeminiDocumentGenerator

router = APIRouter()
generator = GeminiDocumentGenerator()

class DocumentRequest(BaseModel):
    document_type: str = Field(..., min_length=2)
    parties: str = Field(..., min_length=2)
    terms: str = Field(..., min_length=2)
    dates: str = Field(..., min_length=2)
    jurisdiction: str = "Not specified"
    additional_instructions: str = ""

@router.post("/generate")
def generate_document(request: DocumentRequest):
    try:
        document = generator.generate_document(
            document_type=request.document_type,
            parties=request.parties,
            terms=request.terms,
            dates=request.dates,
            jurisdiction=request.jurisdiction,
            additional_instructions=request.additional_instructions,
        )
        return {"success": True, "document": document}
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))
