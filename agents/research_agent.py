from config import tavily_tool

def research_agent(state):
    print(f"\n🔍 Researching: {state['research_query']}")
    try:
        results = tavily_tool.invoke({
            "query": state["research_query"],
            "max_results": 7,
            "time_range": "year"
        })
        return {"raw_data": [result["content"] for result in results]}
    except Exception as e:
        print(f"Research error: {e}")
        return {"raw_data": []}