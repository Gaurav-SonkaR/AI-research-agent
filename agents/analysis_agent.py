from config import llm
import textwrap

def analysis_agent(state):
    print("\n🧠 Analyzing data...")
    context = "\n\n".join(state["raw_data"][-3:])
    
    analysis_prompt = textwrap.dedent(f"""
        As Senior Research Analyst, extract key insights from:
        {context[:3000]}
        
        Required format:
        - Trend identification
        - Statistical highlights
        - Sector-specific developments
        - Government policies
        - Future projections
    """)
    
    response = llm.invoke(analysis_prompt)
    return {"summaries": [response.content]}