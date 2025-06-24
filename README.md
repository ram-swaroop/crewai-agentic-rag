# crewai-agentic-rag
An advanced agentic RAG system built using CrewAI, integrating LangChain with Gemini 2.0 Flash and Ollama based Deepseek-R1:8B models. It performs intelligent routing, vector-based document search (RAG), web search fallback, hallucination grading, and final answer synthesis—all coordinated through autonomous agents.


# Project Structure
```crewai-agentic-rag/
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
|
├── knowledge/
│   └── `add-your-pdf-here`
│
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
  - Deepseek-R1:8B via Ollama (using Local CPU)
  - Gemini 1.5 Flash (via LangChain)

### 🛠️ Run
```bash
python main.py

```bash
python main.py -q "How does DSPy differ from traditional methods of prompting language models in terms of modularity and optimization?"
python main.py -q "Can you explain the role of teleprompters in the DSPy framework and how they contribute to optimizing language model pipelines?"
python main.py -q "What were the key findings from the case studies on math word problems and multi-hop question answering using DSPy?"
python main.py -q "How does DSPy compare to existing libraries like LangChain and LlamaIndex in terms of prompt engineering and modularity?"
python main.py -q "What potential future developments or improvements are suggested for the DSPy framework based on the conclusions of the document?"```
