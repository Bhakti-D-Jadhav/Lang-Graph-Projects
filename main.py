from langgraph.graph import StateGraph, END

from state import InterviewState

from nodes import (
    ask_question,
    get_answer,
    evaluate,
    analyze_performance,
    feedback_node
)

def route(state):

    if state.get("stop"):
        return "end"

    return "continue"

builder = StateGraph(InterviewState)

builder.add_node("question", ask_question)
builder.add_node("answer", get_answer)
builder.add_node("evaluate", evaluate)
builder.add_node("analyze", analyze_performance)
builder.add_node("feedback", feedback_node)

builder.set_entry_point("question")

builder.add_edge("question", "answer")

builder.add_conditional_edges(
    "answer",
    route,
    {
        "continue": "evaluate",
        "end": END
    }
)

builder.add_edge("evaluate", "analyze")
builder.add_edge("analyze", "feedback")
builder.add_edge("feedback", "question")

graph = builder.compile()

if __name__ == "__main__":
    graph.invoke(
        {
            "stop": False
        }
    )