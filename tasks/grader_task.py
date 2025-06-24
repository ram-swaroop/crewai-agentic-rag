from crewai import Task
from agents.grader_agent import Grader_agent
from tasks.retriever_task import retriever_task

grader_task = Task(
    description=(
        "Evaluate whether the retrieved content from retriever_task is relevant to the question {question}. "
        "Return 'yes' if aligned, otherwise 'no'. No explanations."
    ),
    expected_output="'yes' or 'no'",
    agent=Grader_agent,
    context=[retriever_task],
)
