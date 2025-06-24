from crewai.tools import tool
from tools.rag_tool import rag_tool

@tool("router_tool")
def router_tool(question: str) -> str:
    """
    Decide where to route a question: try PDF search first,
    if the PDF has relevant content, return 'vectorstore',
    otherwise return 'web_search'.
    """
    ## run PDF search with a short preview to check relevance
    # preview = rag_tool.run(question, max_results=1, preview=True)
    # if preview and question.lower().split()[0] in preview.lower():
    #     return "vectorstore"
    # return "web_search"

    if 'dspy' in question.lower():
        return 'vectorstore'
    return 'web_search'

