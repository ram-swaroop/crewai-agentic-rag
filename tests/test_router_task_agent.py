from crewai import Crew
from agents.router_agent import Router_Agent
from tasks.router_task import router_task
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

questions = [
    "What is the role of DSPy in AI pipelines?",        # should route to vectorstore
    # "Latest updates on Apple stock today?",             # should route to websearch
]

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
    except Exception as e:
        print(f"❌ Error during task execution: {e}")
