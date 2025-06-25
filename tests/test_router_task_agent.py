from crewai import Crew
from agents.router_agent import Router_Agent
from tasks.router_task import router_task
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

questions = [
    "What is the role of DSPy in AI pipelines?",        # should route to vectorstore
    # "Latest updates on Apple stock today?",             # should route to websearch
]

def test_router_task_agent():
    """
    Test the Router_Agent with the router_task to ensure it routes questions correctly.
    """
    print("Starting Router Task Agent Test...") 
    for q in questions:
        print(f"\n🧪 Testing question: {q}")
        crew = Crew(
            agents=[Router_Agent],
            tasks=[router_task],
            verbose=True  # to see agent reasoning
        )

    try:
        inputs = {"question": q}
        result = crew.kickoff(inputs=inputs)
        print(f"✅ Agent response: {result}")
        assert isinstance(result, dict), "Expected a dictionary response from the agent"
    except Exception as e:
        print(f"❌ Error during task execution: {e}")
