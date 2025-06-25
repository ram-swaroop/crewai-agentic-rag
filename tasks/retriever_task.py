from crewai import Task
from agents.retriever_agent import Retriever_Agent
from tasks.router_task import router_task

retriever_task = Task(
    description=(
        "You are an information retrieval specialist. You will receive the routing decision "
        "from the previous task along with the original question: '{question}'\n\n"
        "Based on the routing decision from the router task:\n"
        "- If the decision was 'vectorstore': Use rag_tool to search documents\n"
        "- If the decision was 'websearch': Use web_search_tool to search current web information\n\n"
        "Provide a comprehensive answer to the user's question based on the retrieved information."
    ),
    expected_output="A comprehensive answer to the user's question based on the retrieved information",
    agent=Retriever_Agent,
    context=[router_task]  # This task depends on router_task output
)
