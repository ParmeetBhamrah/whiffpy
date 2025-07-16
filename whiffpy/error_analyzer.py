import re

def analyze_error(traceback_str: str) -> dict:
    ERROR_HINTS = {
        "ZeroDivisionError": "You tried to divide by zero. Python doesn't allow that. Check your denominator.",
        "NameError": "You're using a variable that hasn't been defined yet.",
        "TypeError": "You're combining values of different types (e.g., int + str).",
        "SyntaxError": "There's a mistake in the structure of your code — maybe a missing colon or quote.",
        "IndexError": "You're accessing an index that doesn't exist in a list or string.",
        "IndentationError": "Your code indentation is off. Python needs consistent spacing.",
    }

    lines = [line for line in traceback_str.strip().split('\n') if line.strip()]
    last_line = lines[-1]

    parts = last_line.split(':')
    err_type = parts[0].strip()
    err_msg = parts[1].strip() if len(parts) > 1 else ""

    line_num = None
    match = re.search(r'line\s+(\d+)', traceback_str)
    if match:
        line_num = int(match.group(1))

    return {
        "type": err_type,
        "message": err_msg,
        "line": line_num,
        "suggestion": ERROR_HINTS.get(err_type, "No specific suggestion available. Try reviewing the error message carefully.")
    }
