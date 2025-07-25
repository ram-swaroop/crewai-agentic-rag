from crewai import Task
from agents.answer_grader import answer_grader
from tasks.hallucination_task import hallucination_task
from tasks.retriever_task import retriever_task

answer_task = Task(
    description=(
        "Evaluate if the answer is valid based on hallucination_task's result for the question {question}. "
        "If 'yes', return a concise answer. If 'no', use web_search_tool and return comprehensive answer to the user's question based on the web search results"
        "If neither, return 'Sorry! unable to find a valid response'."
    ),
    expected_output=(
        "Concise final answer if valid, else web search result, "
        "or fallback message if no good response found."
    ),
    agent=answer_grader,
    context=[retriever_task, hallucination_task],
)
