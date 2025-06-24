from tools.web_search_tool import web_search_tool
from dotenv import load_dotenv
import os
load_dotenv()


def test_web_search_tool():
    """
    Test the web search tool with a sample query.
    """
    # Ensure the environment variable is set
    assert os.getenv("TAVILY_API_KEY"), "TAVILY_API_KEY must be set in .env file"

    # Run the web search tool with a sample query
    response = web_search_tool.run("who won recent ind vs eng test match")
    # print(response)

    assert isinstance(response, (str, dict)), "Unexpected response type"