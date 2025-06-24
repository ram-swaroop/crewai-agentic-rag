from crewai import Agent
from config.settings import llm

Retriever_Agent = Agent(
    role="Retriever",
    goal="Use the appropriate tool to retrieve relevant information for the given question.",
    backstory=(
        "You are responsible for retrieving accurate information from either a vectorstore (PDFs) or the web. "
        "Your job is to use the best-suited tool as directed by the router to answer user queries."
    ),
    verbose=True,
    allow_delegation=False,
    llm=llm,
)
