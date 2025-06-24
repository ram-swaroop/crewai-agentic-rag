import os
from crewai import Agent
from config.settings import llm

answer_grader = Agent(
    role="Answer Grader",
    goal="Filter out hallucination from the answer.",
    backstory=(
        "You assess whether the answer makes sense and is useful. "
        "If it's not, trigger a fallback web search and attempt to generate a more grounded response."
    ),
    verbose=True,
    allow_delegation=False,
    llm=llm,
)
