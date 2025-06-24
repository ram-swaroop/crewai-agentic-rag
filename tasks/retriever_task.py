from crewai import Task
from agents.retriever_agent import Retriever_Agent
from tasks.router_task import router_task

retriever_task = Task(
    description=(
        "Based on the output from router_task, retrieve information for the question {question}. "
        "Use 'web_search_tool' if the router output is 'websearch'. "
        "Use 'rag_tool' if the output is 'vectorstore'. "
        "Provide a clear and concise response."
    ),
    expected_output="Relevant information retrieved from either vectorstore or web search.",
    agent=Retriever_Agent,
    context=[router_task],
)
