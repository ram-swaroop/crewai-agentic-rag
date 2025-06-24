# from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_tavily import TavilySearch
import os
from dotenv import load_dotenv

load_dotenv()

# TAVILY_API_KEY = os.getenv("TAVILY_API_KEY","Not Set")

# print("TAVILY API Key:", TAVILY_API_KEY)
# web_search_tool = TavilySearchResults(k=3)
web_search_tool = TavilySearch(k=3)
