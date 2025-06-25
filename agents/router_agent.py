from crewai import Agent
from config.settings import llm
from tools.router_tool import router_tool

#test llm response
# try:
#     response = llm.call("Test message: respond with 'OK'")
#     print(f"LLM Test Response: {response}")
# except Exception as e:
#     print(f"LLM Connection Error: {e}")

Router_Agent = Agent(
    role='Router',
    goal='Analyze user questions and determine the best information source',
    backstory=(
        "You are an expert question analyzer who determines whether a question "
        "should be answered using stored documents (vectorstore) or current web information (websearch). "
        "You use the router_tool to make this decision based on question keywords and context."
    ),
    verbose=True,
    allow_delegation=False,
    llm=llm,
    tools=[router_tool],  # Add the router tool
)
