from google.adk import Agent
from ..tools.pdf_tools import pdf_tool

resume_parser_agent = Agent(
    name="ResumeParserAgent",
    model="gemini-1.5-flash",
    instruction="""
    You are a resume parsing expert.
    Extract important information from resume text.
    """,
    tools=[pdf_tool]
)