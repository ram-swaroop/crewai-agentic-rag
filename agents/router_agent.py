from crewai import Agent
from config.settings import llm

Router_Agent = Agent(
    role='Router',
    goal='Route user question to a vectorstore or web search',
    backstory="Expert in routing questions using vector relevance.",
    verbose=True,
    allow_delegation=False,
    llm=llm,
)
