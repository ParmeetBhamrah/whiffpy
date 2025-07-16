from .runner import run_code
from .explainer import explain_structure

def analyze(code: str) -> dict:
    output_and_error = run_code(code)
    explanation = explain_structure(code)

    return {
        "output": output_and_error.get("output", ""),
        "error": output_and_error.get("error", ""),
        "explanation": explanation
    }