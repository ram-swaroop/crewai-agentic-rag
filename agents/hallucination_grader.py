import os
from crewai import Agent
from config.settings import llm

hallucination_grader = Agent(
    role="Hallucination Grader",
    goal="Filter out hallucinations from the answer",
    backstory=(
        "You are a grader that checks if the answer is grounded in facts. "
        "Meticulously verify the answer for accuracy based on the context."
    ),
    verbose=True,
    allow_delegation=False,
    llm=llm,
)
