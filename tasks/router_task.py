from tools.router_tool import router_tool
from agents.router_agent import Router_Agent
from crewai import Task

router_task = Task(
    description=(
        "Analyse the keywords in the question {question} and decide the route."
        "Return either 'vectorstore' or 'websearch'."
    ),
    expected_output="Either 'vectorstore' or 'websearch'",
    agent=Router_Agent,
    tools=[router_tool],
)
