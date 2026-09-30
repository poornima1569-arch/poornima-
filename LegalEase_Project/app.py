import html
import os
import requests
import streamlit as st

from utils.document_formatter import format_docx, format_pdf, format_txt

st.set_page_config(
    page_title="LegalEase",
    page_icon="⚖️",
    layout="wide",
)

API_URL = os.getenv("BACKEND_URL", "http://127.0.0.1:8000")

st.markdown("""
<style>
    .hero {
        padding: 1.2rem 1.5rem;
        border-radius: 18px;
        background: linear-gradient(135deg, #111827, #1f2937);
        color: white;
        margin-bottom: 1rem;
    }
    .hero h1 { margin: 0; }
    .preview {
        background: #111827;
        color: #f9fafb;
        border-radius: 14px;
        padding: 22px;
        max-height: 620px;
        overflow-y: auto;
        white-space: pre-wrap;
        font-family: Georgia, serif;
        line-height: 1.6;
    }
    .notice {
        padding: 10px 14px;
        border-left: 4px solid #f59e0b;
        background: #fffbeb;
        border-radius: 6px;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
<h1>⚖️ LegalEase</h1>
<p>AI-Powered Legal Document Generator</p>
</div>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="notice"><b>Important:</b> LegalEase creates AI-assisted drafts. '
    'It does not replace advice from a qualified legal professional.</div>',
    unsafe_allow_html=True,
)

left, right = st.columns([1, 1.15])

with left:
    st.subheader("Document Details")

    document_type = st.selectbox(
        "Document Type",
        [
            "Employment Contract",
            "Non-Disclosure Agreement (NDA)",
            "Lease Agreement",
            "Freelance Work Contract",
            "Service Agreement",
            "General Agreement",
            "Custom Legal Document",
        ],
    )

    parties = st.text_area(
        "Parties Involved",
        placeholder="Jane Doe (Service Provider), TechNova Inc. (Client)",
        height=100,
    )

    terms = st.text_area(
        "Terms & Conditions",
        placeholder=(
            "Payment within 30 days; Confidentiality must be maintained; "
            "Either party may terminate with 15 days notice"
        ),
        height=150,
    )

    dates = st.text_input("Effective Date", placeholder="April 15, 2026")
    jurisdiction = st.text_input(
        "Jurisdiction (optional)",
        placeholder="State/Country or 'Not specified'",
    )
    additional = st.text_area(
        "Additional Instructions (optional)",
        placeholder="Add any extra requirements for the draft.",
        height=100,
    )

    generate = st.button("✨ Generate Document", type="primary", use_container_width=True)

    if generate:
        if not parties.strip() or not terms.strip() or not dates.strip():
            st.error("Please fill in parties, terms, and effective date.")
        else:
            payload = {
                "document_type": document_type,
                "parties": parties,
                "terms": terms,
                "dates": dates,
                "jurisdiction": jurisdiction or "Not specified",
                "additional_instructions": additional,
            }
            try:
                with st.spinner("Generating your document..."):
                    response = requests.post(
                        f"{API_URL}/generate",
                        json=payload,
                        timeout=90,
                    )
                response.raise_for_status()
                st.session_state["document"] = response.json()["document"]
                st.session_state["doc_type"] = document_type
                st.success("Document generated successfully.")
            except Exception as exc:
                st.error(
                    "Backend connection failed. Start FastAPI first with "
                    "`uvicorn main:app --reload`."
                )
                st.caption(str(exc))

with right:
    st.subheader("Document Preview & Editing")

    if "document" in st.session_state:
        edited = st.text_area(
            "Editable Document",
            value=st.session_state["document"],
            height=520,
            key="editor",
        )
        st.session_state["document"] = edited

        safe = html.escape(edited)
        st.markdown(
            f'<div class="preview">{safe}</div>',
            unsafe_allow_html=True,
        )

        st.write("")
        c1, c2, c3 = st.columns(3)

        with c1:
            st.download_button(
                "⬇️ TXT",
                data=format_txt(edited),
                file_name="legalease_document.txt",
                mime="text/plain",
                use_container_width=True,
            )

        with c2:
            st.download_button(
                "⬇️ DOCX",
                data=format_docx(edited, st.session_state.get("doc_type", "Legal Document")),
                file_name="legalease_document.docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                use_container_width=True,
            )

        with c3:
            st.download_button(
                "⬇️ PDF",
                data=format_pdf(edited, st.session_state.get("doc_type", "Legal Document")),
                file_name="legalease_document.pdf",
                mime="application/pdf",
                use_container_width=True,
            )
    else:
        st.info("Your generated document will appear here.")

st.divider()
st.caption("LegalEase • FastAPI + Streamlit + Gemini • Educational project")
