from google.adk import Agent
from ..tools.keyword_tools import keyword_tool
from ..tools.report_tools import report_tool

keyword_optimizer_agent = Agent(
    name="KeywordOptimizerAgent",
    model="gemini-1.5-flash",
    instruction="""
    Compare resume and job description keywords.
    Suggest missing keywords and improvements.
    Generate final formatted report.
    """,
    tools=[keyword_tool, report_tool]
)