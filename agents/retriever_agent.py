from crewai import Agent
from config.settings import llm
from tools.rag_tool import rag_tool
from tools.web_search_tool import web_search_tool

Retriever_Agent = Agent(
    role='Information Retriever',
    goal='Retrieve relevant information based on routing decision',
    backstory=(
        "You are an information retrieval specialist. Based on the routing decision, "
        "you either search documents using rag_tool or search the web using web_search_tool."
    ),
    verbose=True,
    allow_delegation=False,
    llm=llm,
    tools=[rag_tool, web_search_tool],  # Add both tools
)
