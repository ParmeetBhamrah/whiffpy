from .runner import run_code
from .explainer import explain_structure
from .error_analyzer import analyze_error
from .utils import format_error_analysis, CodeReport

def analyze(code: str) -> dict:
    output_and_error = run_code(code)
    
    try:
        explanation = explain_structure(code)
    except SyntaxError as e:
        error_analysis = analyze_error(str(e))
        return {
            "output": "",
            "error_analysis": error_analysis,
            "status": "Syntax error detected"
        }
    output = output_and_error.get("output", "")
    error = output_and_error.get("error", "")

    formatted_error = None
    
    if error:
        formatted_error = format_error_analysis(analyze_error(error))
        return CodeReport(
            output=output,
            explanation=explanation,
            status="Error found",
            error_analysis=formatted_error
        )
    
    return CodeReport(
        output=output,
        explanation=explanation,
        status="No errors found",
        error_analysis=None,
    )