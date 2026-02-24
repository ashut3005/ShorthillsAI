# Smart Resume Analyzer

This system analyzes a candidate's resume and compares it with a job description.
It identifies missing keywords, suggests improvements, and generates an optimized report.

Architecture:
- Root Agent (Orchestrator)
- Resume Parser Agent
- Job Description Analyzer Agent
- Keyword Optimization Agent

Tools:
- google_search (mandatory)
- extract_pdf_text
- extract_keywords
- generate_report