# crewai-agentic-rag
An advanced agentic RAG system built using CrewAI, integrating LangChain with Gemini 2.0 Flash and Ollama based Qwen2.5:3B models. It performs intelligent routing, vector-based document search (RAG), web search fallback, hallucination grading, and final answer synthesis—all coordinated through autonomous agents.


# Project Structure
```
crewai-agentic-rag/

├── agents/
│   ├── __init__.py
│   ├── router_agent.py
│   ├── retriever_agent.py
│   ├── grader_agent.py
│   ├── hallucination_grader.py
│   ├── answer_grader.py
│
├── tasks/
│   ├── __init__.py
│   ├── router_task.py
│   ├── retriever_task.py
│   ├── grader_task.py
│   ├── hallucination_task.py
│   ├── answer_task.py
│
├── tools/
│   ├── __init__.py
│   ├── rag_tool.py
│   ├── web_search_tool.py
│   ├── router_tool.py
│
├── crew/
│   ├── __init__.py
│   └── crew_setup.py
│
├── knowledge/
│   └── add-your-pdf-here/
│
├── tests/
│   ├── __init__.py
│   ├── test_rag_tool.py
│   ├── test_router_task_agent.py
│   └── test_web_search_tool.py
│
├── config/
│   ├── __init__.py
│   └── settings.py
│
├── .env.example
├── __init__.py
├── main.py
├── requirements.txt
└── README.md

```


### 🚀 Features
- **LLM-Driven Routing**: Directs questions to appropriate retrieval method.
- **PDF (RAG) and Web Search**: Combines structured knowledge with real-time web intelligence.
- **Answer Verification Pipeline**: Includes relevance grading and hallucination detection.
- **LLMs Used**:
  - Qwen2.5:3B via Ollama (using Local CPU)
  - Gemini 2.0 Flash (via LangChain)

---

## 🚀 Quick Start

### ▶️ Run with Python

```bash
# 1. Install dependencies (requires Python 3.12.8)
pip install -r requirements.txt

# 2. Run analysis
python main.py

# Examples
python main.py -q "How does DSPy differ from traditional methods of prompting language models in terms of modularity and optimization?" # [should use knowledge base]
python main.py -q "How does DSPy compare to existing libraries like LangChain and LlamaIndex in terms of prompt engineering and modularity?" # [should use knowledge base]
python main.py -q "Which teams qualified for round-16 in recent fifa club worldcup?"``` # [should use web search]

# 3. Run tests
pytest
```

## ✅ Python Version

This project uses and expects **Python 3.12.8**.

## 📈 Example Outputs

Want to see how this system responds to user queries?

Check out:  
[`examples/output_samples.md`](examples/output_samples.md)

This includes responses from gemini-2.0-flash only:
- Google Gemini `gemini-2.0-flash` (cloud-based via Free API Key)

## ⚙️ LLM Compatibility Observations (CrewAI Agents)

### ✅ Working as Expected
- **Google Gemini 2.0 Flash**
  - ✅ Works perfectly with `CrewAI` agents using `crewai.LLM`, both:
    - When called **independently**:  
      ```python
      llm.call("Test message")
      ```
    - When used **inside CrewAI agents**:
      ```python
      Agent(..., llm=llm, ...)
      ```

### ⚠️ Issues Observed
- **Local models via Ollama** (e.g., `qwen2.5`, `deepseek-coder`)
  - ✅ Works when called **independently** using `crewai.LLM`:
    ```python
    llm.call("Test message")
    ```
  - ❌ **Fails when used inside CrewAI agents**:
    - Error encountered:
      ```
      LLM Failed Error
      ```
    - Indicates potential issues with local model integration in agent context (e.g., serialization, networking, tool wrapping or api integration etc).


