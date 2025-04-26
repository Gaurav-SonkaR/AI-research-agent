from config import MAX_ITERATIONS

def validation_agent(state):
    print(f"\n✅ Validation check (Iteration {state.get('iteration_count', 0)+1}/{MAX_ITERATIONS})")
    summary = state["summaries"][-1]
    
    # Force finalization if max iterations reached
    if state.get("iteration_count", 0) >= MAX_ITERATIONS - 1:
        print("⚠️ Maximum iterations reached, auto-finalizing")
        return {"validation": True}
    
    validation_prompt = f"""
    Current summary:
    {summary}
    
    Should we:
    1. Finalize (1)
    2. Improve (2)
    3. Restart research (3)
    """
    
    while True:
        choice = input(validation_prompt).strip().lower()
        if choice in ["1", "y", "yes"]:
            return {"validation": True}
        elif choice in ["2", "improve"]:
            return {"validation": False}
        elif choice in ["3", "restart"]:
            return {"validation": "restart"}
        print("Invalid choice. Please enter 1, 2, or 3")