import ast

class CodeExplainer(ast.NodeVisitor):
    """
    AST-based analyzer that traverses user code and extracts
    high-level explanations about its structure.

    Attributes:
        explanations (list): Textual descriptions of code elements found,
                             such as loops, assignments, function calls, etc.
    """

    def __init__(self):
        self.explanations = []

    def visit_FunctionDef(self, node):
        self.explanations.append(f"defines a function named '{node.name}'")
        # detect parameters
        if node.args.args:
            params = ", ".join(arg.arg for arg in node.args.args)
            self.explanations.append(f"function '{node.name}' takes parameter(s): {params}")
        self.generic_visit(node)

    def visit_ClassDef(self, node):
        self.explanations.append(f"defines a class named '{node.name}'")
        self.generic_visit(node)

    def visit_Return(self, node):
        self.explanations.append("uses a return statement")
        self.generic_visit(node)

    def visit_Assign(self, node):
        for target in node.targets:
            if isinstance(target, ast.Name):
                self.explanations.append(f"assigns a variable named '{target.id}'")
        self.generic_visit(node)

    def visit_AugAssign(self, node):
        if isinstance(node.target, ast.Name):
            op = node.op.__class__.__name__.replace("Add", "+").replace("Sub", "-")\
                                              .replace("Mult", "*").replace("Div", "/")
            self.explanations.append(f"updates '{node.target.id}' with an augmented assignment (e.g., {node.target.id} {op}= ...)")
        self.generic_visit(node)

    def visit_For(self, node):
        self.explanations.append("uses a for loop")
        self.generic_visit(node)

    def visit_While(self, node):
        self.explanations.append("uses a while loop")
        self.generic_visit(node)

    def visit_If(self, node):
        self.explanations.append("uses an if statement")
        self.generic_visit(node)

    def visit_With(self, node):
        self.explanations.append("uses a with statement (context manager)")
        self.generic_visit(node)

    def visit_Import(self, node):
        modules = ", ".join(alias.name for alias in node.names)
        self.explanations.append(f"imports module(s): {modules}")
        self.generic_visit(node)

    def visit_ImportFrom(self, node):
        mod = node.module or ""
        names = ", ".join(alias.name for alias in node.names)
        self.explanations.append(f"imports {names} from module '{mod}'")
        self.generic_visit(node)

    def visit_Expr(self, node):
        # catch bare calls like print(...)
        if isinstance(node.value, ast.Call):
            self.visit_Call(node.value)
        self.generic_visit(node)

    def visit_Call(self, node):
        func = getattr(node.func, "id", None) or getattr(node.func, "attr", None)
        if func == "print":
            self.explanations.append("uses a print statement")
        else:
            self.explanations.append(f"calls the function '{func}'")
        self.generic_visit(node)

    def visit_Compare(self, node):
        ops = [type(op).__name__ for op in node.ops]
        self.explanations.append(f"performs a comparison using {', '.join(ops)}")
        self.generic_visit(node)

    def visit_BinOp(self, node):
        op = node.op.__class__.__name__
        self.explanations.append(f"performs a binary operation: {op}")
        self.generic_visit(node)

    def visit_Attribute(self, node):
        self.explanations.append(f"accesses attribute '{node.attr}'")
        self.generic_visit(node)

    def visit_ListComp(self, node):
        self.explanations.append("uses a list comprehension")
        self.generic_visit(node)

    def visit_DictComp(self, node):
        self.explanations.append("uses a dictionary comprehension")
        self.generic_visit(node)

    def visit_SetComp(self, node):
        self.explanations.append("uses a set comprehension")
        self.generic_visit(node)

    def visit_GeneratorExp(self, node):
        self.explanations.append("uses a generator expression")
        self.generic_visit(node)

    def visit_Try(self, node):
        self.explanations.append("uses a try block for exception handling")
        self.generic_visit(node)

    def visit_ExceptHandler(self, node):
        err = node.type.id if isinstance(node.type, ast.Name) else "Exception"
        self.explanations.append(f"handles exceptions of type '{err}'")
        self.generic_visit(node)

    def visit_Assert(self, node):
        self.explanations.append("uses an assert statement for debugging checks")
        self.generic_visit(node)

    def visit_Lambda(self, node):
        self.explanations.append("defines an anonymous function (lambda)")
        self.generic_visit(node)

    def visit_Constant(self, node):
        val = node.value
        t = type(val).__name__
        self.explanations.append(f"uses a constant of type '{t}' with value {repr(val)}")

    def visit_List(self, node):
        self.explanations.append("builds a list literal")
        self.generic_visit(node)

    def visit_Tuple(self, node):
        self.explanations.append("builds a tuple literal")
        self.generic_visit(node)

    def visit_Dict(self, node):
        self.explanations.append("builds a dictionary literal")
        self.generic_visit(node)

    def visit_Set(self, node):
        self.explanations.append("builds a set literal")
        self.generic_visit(node)

    # fallback
    def generic_visit(self, node):
        super().generic_visit(node)

def explain_structure(code: str) -> str: 
    """
    Analyzes Python code and returns a human-readable description
    of its structure using AST. If the code has a syntax error, 
    returns a helpful hint with location info.

    Args:
        code (str): Python code to analyze.

    Returns:
        str: Structural description or syntax error feedback.
    """
    
    tree = ast.parse(code)
    explainer = CodeExplainer()
    explainer.visit(tree)
    return "This code:\n" + "\n".join(f"- {exp}" for exp in explainer.explanations)
