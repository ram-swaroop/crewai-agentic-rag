import os
from crewai import Agent
from config.settings import llm
from tools.web_search_tool import web_search_tool

answer_grader = Agent(
    role="Final Answer Generator",
    goal="Filter out hallucination from the answer.",
    backstory=(
        "You assess whether the answer was grounded with facts based on response from hallunication grader"
        "If it was grounded with facts [Yes], return a concise answer."
        "If it was not grounded with facts [No], use web_search_tool to find a more accurate answer."
    ),
    verbose=True,
    allow_delegation=False,
    llm=llm,
    tools=[web_search_tool],  # Uncomment if web search tool is needed
)
