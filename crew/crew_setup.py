from agents.router_agent import Router_Agent
from agents.retriever_agent import Retriever_Agent
from agents.grader_agent import Grader_agent
from agents.hallucination_grader import hallucination_grader
from agents.answer_grader import answer_grader

from tasks.router_task import router_task
from tasks.retriever_task import retriever_task
from tasks.grader_task import grader_task
from tasks.hallucination_task import hallucination_task
from tasks.answer_task import answer_task

from crewai import Crew

rag_crew = Crew(
    agents=[
        Router_Agent,
        Retriever_Agent,
        Grader_agent,
        hallucination_grader,
        answer_grader
    ],
    tasks=[
        router_task,
        retriever_task,
        grader_task,
        hallucination_task,
        answer_task
    ],
    verbose=True
)
