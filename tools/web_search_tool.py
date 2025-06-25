# tools/web_search_tool.py
import os
from langchain_tavily import TavilySearch
from crewai.tools import tool
from dotenv import load_dotenv

load_dotenv()

# Initialize Tavily search tool
top_n = 10
tavily = TavilySearch(
    max_results=top_n,
    # include_answer=True,
    include_raw_content=True,
    include_images=False,
)

# Wrap the tool using CrewAI's decorator
@tool("web_search_tool")
def web_search_tool(query: str) -> dict:
    """
    Perform a real-time web search using Tavily.
    Returns raw dictionary of results.
    """
            # Search for current information
    response = tavily.run(query)
        
    if not response.get('results'):
        return f"No current information found for: {query}"
    
    # Format results
    results = []
    for item in response['results']:  # Top 3 results
        # print(f"Processing item: {item.keys()}")
        # print(f"Processing item: {item}")
        title = item.get('title', 'No title')
        content = item.get('content', 'No content')
        # raw_content = item.get('raw_content', 'No raw_content')
        # print(f"content: {len(content)}")
        # print(f"Raw content: {len(raw_content)}")
        url = item.get('url', 'No URL')
        results.append(f"**{title}**\n{content}\nSource: {url}\n")
        # results.append(f"**{title}**\n{raw_content}\nSource: {url}\n")
    
    return "\n".join(results)

    # return tavily.run(query)
