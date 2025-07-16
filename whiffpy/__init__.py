from .runner import run_code
from .explainer import explain_structure
from .error_analyzer import analyze_error

def analyze(code: str) -> dict:
    output_and_error = run_code(code)
    explanation = explain_structure(code)

    error_analysis = None
    if output_and_error.get("error"):
        error_analysis = analyze_error(output_and_error["error"])

    return {
        "output": output_and_error.get("output", ""),
        "error": output_and_error.get("error", ""),
        "error_analysis": error_analysis,
        "explanation": explanation
    }