from crewai import Task
from agents.hallucination_grader import hallucination_grader
from tasks.grader_task import grader_task

hallucination_task = Task(
    description=(
        "Evaluate if the answer from the retriever is grounded in facts and useful to answer {question}. "
        "Return 'yes' if the answer is fact-based and helpful, otherwise 'no'."
    ),
    expected_output="'yes' or 'no'",
    agent=hallucination_grader,
    context=[grader_task],
)
