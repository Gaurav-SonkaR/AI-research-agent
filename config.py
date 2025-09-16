from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults
from dotenv import load_dotenv
import os

load_dotenv()

# Model configuration
MODEL_NAME = "deepseek/deepseek-r1"
MAX_ITERATIONS = 10
MAX_RECURSION = 15
RESEARCH_DOMAINS = ["gov.in", "economictimes.indiatimes.com", "investindia.gov.in","https://en.wikipedia.org/wiki/"]

# Initialize core components
llm = ChatOpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    model=MODEL_NAME,
    temperature=0.3
)

tavily_tool = TavilySearchResults(
    api_key=os.getenv("TAVILY_API_KEY"),
    max_results=7,
    search_depth="advanced",
    include_domains=RESEARCH_DOMAINS

)
