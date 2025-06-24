from langchain_community.tools.tavily_search import TavilySearchResults
import os

# Tavily API Key is aleady set in the .env file
web_search_tool = TavilySearchResults(k=3)
