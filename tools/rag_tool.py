# tools/rag_tool.py
import os
from dotenv import load_dotenv
from crewai.tools import tool
from crewai_tools import PDFSearchTool

load_dotenv()

# Initialize the PDFSearchTool (no llm=… object passed)
pdf_search = PDFSearchTool(
    pdf="knowledge/dspy.pdf",
    config=dict(
        llm=dict(
            provider=os.getenv("LLM_PROVIDER", "google"),
            config=dict(model=os.getenv("LLM_MODEL", "gemini-2.0-flash")),
        ),
        embedder=dict(
            provider="huggingface",
            config={
                "model": os.getenv("EMBEDDER_MODEL", "BAAI/bge-small-en-v1.5"),
                **({"api_key": os.getenv("HUGGINGFACE_API_KEY")} if os.getenv("HUGGINGFACE_API_KEY") else {})
            },
        ),
    )
)

@tool("rag_tool")
def rag_tool(question: str) -> str:
    """
    Search the PDF (dspy.pdf) and return the most relevant excerpt or summary for the question.
    """
    return pdf_search.run(question)
