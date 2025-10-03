import re
from .utils import ERROR_HINTS

def analyze_error(traceback_str: str) -> dict:
    """
    Interprets a Python error traceback and returns a structured, human-friendly
    error description.

    Args:
        traceback_str (str): The raw traceback string from code execution.

    Returns:
        dict: Contains error type, message, line number, and a helpful suggestion.
    """

    lines = [line for line in traceback_str.strip().split('\n') if line.strip()]
    last_line = lines[-1]

    parts = last_line.split(':')
    err_type = parts[0].strip()
    err_msg = parts[1].strip() if len(parts) > 1 else ""

    line_num = None
    # Prefer the innermost frame's line number from standard traceback lines like:
    #   File "<string>", line 3, in <module>
    frame_matches = re.findall(r'File\s+"([^"]+)",\s+line\s+(\d+)', traceback_str)
    if frame_matches:
        # take the last (innermost) frame
        _, ln = frame_matches[-1]
        try:
            line_num = int(ln)
        except ValueError:
            line_num = None
    else:
        # fallback: search for any 'line N' occurrence
        match = re.search(r'line\s+(\d+)', traceback_str)
        if match:
            line_num = int(match.group(1))

    return {
        "type": err_type,
        "message": err_msg,
        "line": line_num,
        "suggestion": ERROR_HINTS.get(err_type, "No specific suggestion available. Try reviewing the error message carefully.")
    }