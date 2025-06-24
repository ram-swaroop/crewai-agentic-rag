from crew.crew_setup import rag_crew
from dotenv import load_dotenv
import argparse

load_dotenv()

# inputs = {"question": "Does the ESOP supplement the salary of an employee?"}
# result = rag_crew.kickoff(inputs=inputs)
# print(result)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run the RAG Crew with specified inputs.")
    parser.add_argument("--question","-q", type=str, help="The question to be processed by the Crew Agent", required=True)

    args = parser.parse_args()
    inputs = {"question": args.question}
    results = rag_crew.kickoff(inputs=inputs)
    print(f"Final Answer: {results}")
    # print("RAG Crew has completed its tasks.")