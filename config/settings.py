import os
from dotenv import load_dotenv
from crewai import LLM

load_dotenv()


LLM_PROVIDER = os.getenv("LLM_PROVIDER","google")

if LLM_PROVIDER == "ollama":
    ollama_model = os.getenv("LLM_MODEL", "qwen2.5:3b")
    llm = LLM(
            model=f"ollama/{ollama_model}",
            temperature=0.2,
            base_url="http://localhost:11434"
        )
    # response = llm.call(
    # "Analyze the following messages and return the name, age, and breed. "
    # "Meet Kona! She is 3 years old and is a black german shepherd."
    # )
    # print(response)
elif LLM_PROVIDER == "google":
    gemini_model = os.getenv("LLM_MODEL", "gemini-2.0-flash")
    llm = LLM(
        model=f"gemini/{gemini_model}",
        temperature=0.2,
        google_api_key=os.getenv("GEMINI_API_KEY")
    )
    # response = llm.call(
    # "Analyze the following messages and return the name, age, and breed. "
    # "Meet Kona! She is 3 years old and is a black german shepherd."
    # )
    # print(response)
else:
    raise ValueError(f"Unsupported LLM_PROVIDER: {LLM_PROVIDER}")


# --- Embedder Config ---
EMBEDDER_PROVIDER = os.getenv("EMBEDDER_PROVIDER", "huggingface")
EMBEDDER_MODEL = os.getenv("EMBEDDER_MODEL", "BAAI/bge-small-en-v1.5")
HF_API_KEY = os.getenv("HUGGINGFACE_API_KEY", None)

EMBEDDER_CONFIG = {
    "provider": EMBEDDER_PROVIDER,
    "config": {
        "model": EMBEDDER_MODEL,
        **({"api_key": HF_API_KEY} if HF_API_KEY else {})
    }
}