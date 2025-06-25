from tools.rag_tool import rag_tool
from dotenv import load_dotenv
import os
load_dotenv()


def test_rag_tool():
    """
    Test the RAG tool with a sample query.
    """
    # Run the RAG tool with a sample query
    response = rag_tool.run("How does DSPy differ from traditional methods of prompting language models in terms of modularity and optimization?")
    print(response)

    assert isinstance(response, (str, dict)), "Unexpected response type"
    # assert isinstance(response, (int, float)), "Unexpected response type"