# from tools.router_tool import router_tool
from agents.router_agent import Router_Agent
from crewai import Task

router_task = Task(
    description=(
        "Analyze the user question: '{question}'\n"
        "Use the router_tool to determine the best information source.\n"
        "Return ONLY the routing decision as a single word."
    ),
    expected_output="A single word: either 'vectorstore' or 'websearch'",
    agent=Router_Agent,
    output_direct=True
    # tools=[router_tool],
)
