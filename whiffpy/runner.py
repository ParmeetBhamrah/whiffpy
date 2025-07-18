import sys
from io import StringIO
import traceback

def run_code(code: str) -> dict:
    """
    Executes Python code in an isolated environment,
    capturing standard output and any runtime errors.

    Args:
        code (str): A Python code string to execute.

    Returns:
        dict: A dictionary with two keys:
              - 'output': Printed output from the code.
              - 'error': Traceback or error message, if an error occurred.
    """

    output_buffer = StringIO()
    error_buffer = StringIO()

    og_stdout, og_stderr = sys.stdout, sys.stderr
    sys.stdout, sys.stderr = output_buffer, error_buffer

    try:
        exec(code, {})
    except Exception:
        error_buffer.write(traceback.format_exc())
    finally:
        sys.stdout, sys.stderr = og_stdout, og_stderr

    return {
        "output": output_buffer.getvalue(),
        "error": error_buffer.getvalue()
    }