from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["message"] == "LegalEase API is running"

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_generate_without_api_key():
    payload = {
        "document_type": "Freelance Work Contract",
        "parties": "Jane Doe (Provider), TechNova Inc. (Client)",
        "terms": "Payment within 30 days; Confidentiality required",
        "dates": "September 28, 2026",
        "jurisdiction": "Not specified",
        "additional_instructions": "",
    }
    response = client.post("/generate", json=payload)
    assert response.status_code == 200
    body = response.json()
    assert body["success"] is True
    assert "FREELANCE WORK CONTRACT" in body["document"]
