from google.adk.tools import FunctionTool

def generate_report(data: str) -> str:
    """
    Generate formatted improvement report.
    """
    return f"""
    ===== SMART RESUME ANALYSIS REPORT =====
    
    {data}
    
    ========================================
    """

report_tool = FunctionTool.from_function(generate_report)