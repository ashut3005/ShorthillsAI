from google.adk import Agent

from .sub_agents.resume_parser import resume_parser_agent
from .sub_agents.jd_analyzer import jd_analyzer_agent
from .sub_agents.keyword_optimizer import keyword_optimizer_agent

root_agent = Agent(
    name="SmartResumeAnalyzerRoot",
    model="gemini-1.5-flash",
    instruction="""
    You are the orchestrator.
    
    Steps:
    1. Call ResumeParserAgent
    2. Call JDAnalyzerAgent
    3. Call KeywordOptimizerAgent
    4. Return final report
    """,
    sub_agents=[
        resume_parser_agent,
        jd_analyzer_agent,
        keyword_optimizer_agent
    ]
)