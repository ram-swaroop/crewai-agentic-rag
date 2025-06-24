from crewai_tools import PDFSearchTool
from config.settings import llm
import os

# from dotenv import load_dotenv
# load_dotenv()

rag_tool = PDFSearchTool(
    pdf="knowledge\dspy.pdf",
    config=dict(
        # llm={"google": "crewai", "config": {}},  # Not used internally here
        llm=dict(
            provider=os.getenv("LLM_PROVIDER", "google"),
            config=dict(
                model=os.getenv("LLM_MODEL", "gemini-2.0-flash")
            )),
        embedder=dict(
            provider="huggingface",
            config={"model": "BAAI/bge-small-en-v1.5"},
        ),
    ),    
    llm=llm # pass your configured CrewAI Gemini LLM object
)
