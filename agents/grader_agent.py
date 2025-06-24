import os
from crewai import Agent
from config.settings import llm

Grader_agent = Agent(
    role='Answer Grader',
    goal='Filter out erroneous retrievals',
    backstory=(
        "You are a grader assessing relevance of a retrieved document to a user question. "
        "You grade it as relevant if it contains keywords related to the user query."
    ),
    verbose=True,
    allow_delegation=False,
    llm=llm,
)
