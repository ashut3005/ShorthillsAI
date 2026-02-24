# Smart Resume Analyzer (Google ADK)

## Description
This multi-agent system analyzes a resume against a job description
and suggests keyword improvements using Google ADK.

## Architecture
- Root Agent (Orchestrator)
- Resume Parser Agent
- JD Analyzer Agent
- Keyword Optimizer Agent

## Setup

1. Create virtual environment
2. Install requirements:
   pip install -r requirements.txt

3. Add .env file:
   GOOGLE_API_KEY=your_key_here

## Run

CLI Mode:
adk run smart_resume_analyzer

Web Mode:
adk web