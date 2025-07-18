ERROR_HINTS = {
    # Syntax and Indentation
    "SyntaxError": "There's a mistake in your code syntax—check for missing colons, quotes, or unmatched parentheses.",
    "IndentationError": "Your code indentation is off. Python requires consistent spacing for blocks.",
    "TabError": "You mixed tabs and spaces in your indentation. Pick one and stick with it.",

    # Name and Binding
    "NameError": "You're using a name (variable or function) that hasn't been defined yet.",
    "UnboundLocalError": "A local variable is referenced before assignment—make sure you assign it before use.",

    # Type and Value
    "TypeError": "Operation on incompatible types—check that you're not, for example, adding a string to a number.",
    "ValueError": "A function got a valid type but an invalid value—check the data you passed into it.",
    "OverflowError": "A numeric result is too large to represent—consider using a different approach or data type.",
    "ZeroDivisionError": "You tried to divide by zero. Python doesn’t allow that—ensure your denominator isn’t zero.",
    "AssertionError": "An assert statement failed—verify the condition you're asserting is actually true.",

    # Lookup
    "IndexError": "You're accessing a sequence index that doesn't exist—check your list/string length.",
    "KeyError": "You're trying to get a dictionary key that isn’t there—verify the key or use dict.get().",
    "StopIteration": "You reached the end of an iterator—there are no more items to retrieve.",

    # Attribute and Import
    "AttributeError": "You're accessing an attribute or method that this object doesn’t have—check the object’s type.",
    "ImportError": "Python couldn't import something—check the module or symbol name and that it’s installed.",
    "ModuleNotFoundError": "No module named as specified—make sure it's installed and spelled correctly.",

    # File and I/O
    "FileNotFoundError": "The file you're trying to open doesn't exist—check the path and filename.",
    "EOFError": "Input ended unexpectedly (end-of-file). If using input(), ensure there’s data to read.",

    # System and Runtime
    "RuntimeError": "A generic runtime error occurred—check your code logic around where it failed.",
    "MemoryError": "Your program ran out of memory—try using less data or optimizing your data structures.",
    "RecursionError": "You exceeded the maximum recursion depth—add a base case or convert recursion to iteration.",
    "KeyboardInterrupt": "Execution was interrupted (e.g., you pressed Ctrl+C).",

    # Specialized
    "NotImplementedError": "A feature or method isn’t implemented yet—provide an implementation before calling it.",
    "AssertionError": "An assert statement failed—check the boolean expression you provided.",
}

def format_error_analysis(error_info: dict) -> str:
    """
    Converts a structured error dictionary into a readable error explanation.

    Args:
        error_info (dict): A dictionary containing error metadata,
                           including type, message, line, and suggestion.

    Returns:
        str: A formatted string with the error type, location, and advice.
    """

    if not error_info or not isinstance(error_info, dict):
        return "An unknown error occurred."
    
    error_type = error_info.get("type", "UnknownError")
    message = error_info.get("message", "No message available.")
    line = error_info.get("line", "Unknown line")
    suggestion = error_info.get("suggestion", "")

    explanation = f"{error_type} at line {line}: {message}"
    if suggestion:
        explanation += f"\nSuggestion: {suggestion}"

    return explanation

class CodeReport:
    """
    Holds the results of analyzing user code, including output,
    structure explanation, error insights, and status messages.

    Attributes:
        output (str): Captured stdout from the code.
        explanation (str): Structural breakdown from AST analysis.
        status (str): Success or error summary.
        error_analysis (str): Friendly error message, if applicable.
    """

    def __init__(self, output:str, explanation:str, status: str = "No errors found", error_analysis: str = None):
        self.output = output
        self.explanation = explanation
        self.status = status
        self.error_analysis = error_analysis

    def __str__(self):
        sections = [
            f"Output:\n{self.output or '(no output)'}",
            f"Explanation:\n{self.explanation.strip() or '(no explanation)'}"
        ]

        if self.error_analysis:
            sections.append(f"Error Analysis:\n{self.error_analysis}")
        elif self.status:
            sections.append(f"Status:\n{self.status}")

        return "\n\n".join(sections)
    
    def to_dict(self):
        return {
            "output": self.output,
            "explanation": self.explanation,
            "status": self.status,
            "error_analysis": self.error_analysis,
        }