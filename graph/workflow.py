from langgraph.graph import StateGraph, END
from typing import TypedDict, Annotated, Sequence
import operator
from agents import research_agent, analysis_agent, validation_agent, human_feedback
from config import MAX_ITERATIONS

class AgentState(TypedDict):
    research_query: str
    raw_data: Annotated[Sequence[str], operator.add]
    summaries: Annotated[Sequence[str], operator.add]
    validation: bool
    iteration_count: int

def create_workflow():
    workflow = StateGraph(AgentState)

    # Wrap research agent to track iterations
    def wrapped_research_agent(state):
        result = research_agent.research_agent(state)
        return {**result, "iteration_count": state.get("iteration_count", 0) + 1}

    # Add nodes with iteration handling
    workflow.add_node("research", wrapped_research_agent)
    workflow.add_node("analyze", analysis_agent.analysis_agent)
    workflow.add_node("validate", validation_agent.validation_agent)
    workflow.add_node("human_input", human_feedback.human_feedback)

    # Set up edges
    workflow.set_entry_point("research")
    workflow.add_edge("research", "analyze")
    workflow.add_edge("analyze", "validate")

    # Enhanced conditional edges
    def route_decision(state):
        if state.get("iteration_count", 0) >= MAX_ITERATIONS:
            return "force_end"
        if state["validation"] is True:
            return "continue"
        elif state["validation"] == "restart":
            return "restart"
        else:
            return "improve"

    workflow.add_conditional_edges(
        "validate",
        route_decision,
        {
            "continue": END,
            "improve": "human_input",
            "restart": "research",
            "force_end": END
        }
    )

    workflow.add_edge("human_input", "research")
    
    return workflow.compile()

app = create_workflow()