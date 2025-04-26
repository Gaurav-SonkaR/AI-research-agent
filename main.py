from graph.workflow import app
from config import MAX_ITERATIONS
from config import MAX_RECURSION

def main():
    query = input("Enter research topic: ")
    
    results = app.invoke({
        "research_query": query,
        "raw_data": [],
        "summaries": [],
        "validation": False,
        "iteration_count": 0
    }, {"recursion_limit": MAX_RECURSION})
    
    print("\n📊 Final Report:")
    print(results["summaries"][-1])

if __name__ == "__main__":
    main()