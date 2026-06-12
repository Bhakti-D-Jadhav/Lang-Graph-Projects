from typing import TypedDict

class InterviewState(TypedDict):        # Defines structure and distionary
    q: str
    topic: str
    a: str
    score: int
    feedback: str
    avg_score: float
    difficulty: str
    stop: bool