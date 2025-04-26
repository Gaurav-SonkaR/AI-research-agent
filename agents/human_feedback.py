def human_feedback(state):
    feedback = input("\n👤 Provide improvement suggestions: ")
    return {"research_query": f"{state['research_query']} [User Feedback: {feedback}]"}