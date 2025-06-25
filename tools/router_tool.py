from crewai.tools import tool
from tools.rag_tool import rag_tool

@tool("router_tool")
def router_tool(question: str) -> str:
    """
    Decide where to route a question: try PDF search first,
    Returns 'vectorstore' for PDF-related queries, 'websearch' for general/recent queries.
    """
    ## run PDF search with a short preview to check relevance
    # preview = rag_tool.run(question, max_results=1, preview=True)
    # if preview and question.lower().split()[0] in preview.lower():
    #     return "pdf_search"
    # return "web_search"

    # 1. PDF-specific keywords
    pdf_keywords = ['dspy', 'rag', 'architecture', 'framework', 'pipeline', 'module', 'agentic', 'embedding']
    if any(keyword in question.lower() for keyword in pdf_keywords):
        return 'vectorstore'
    # if 'dspy' in question.lower():
    #     return 'vectorstore'
    return 'websearch'

