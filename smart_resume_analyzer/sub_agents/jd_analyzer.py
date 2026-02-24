from google.adk import Agent
from google.adk.tools import google_search

jd_analyzer_agent = Agent(
    name="JDAnalyzerAgent",
    model="gemini-1.5-flash",
    instruction="""
    Analyze the job description and identify required skills.
    Use google_search if needed to understand industry requirements.
    """,
    tools=[google_search]
)