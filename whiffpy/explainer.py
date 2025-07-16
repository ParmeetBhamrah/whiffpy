import ast

class CodeExplainer(ast.NodeVisitor):
    def __init__(self):
        self.explanations = []

    def visit_FunctionDef(self, node):
        self.explanations.append(f"defines a function named '{node.name}'")
        self.generic_visit(node)

    def visit_Assign(self, node):
        for target in node.targets:
            if isinstance(target, ast.Name):
                self.explanations.append(f"assigns a variable named '{target.id}'")
        self.generic_visit(node)

    def visit_For(self, node):
        self.explanations.append("uses a for loop")
        self.generic_visit(node)

    def visit_If(self, node):
        self.explanations.append("uses an if statement")
        self.generic_visit(node)

    def visit_While(self, node):
        self.explanations.append("uses a while loop")
        self.generic_visit(node)

    def visit_With(self, node):
        self.explanations.append("uses a with statement")
        self.generic_visit(node)

def explain_structure(code: str) -> str:    
    try:
        tree = ast.parse(code)
    except SyntaxError as e:
        return f"""
                Invalid Syntax!\n
                You have a syntax error at the\n
                {e.offset}th character of line {e.lineno}\n
                >>{e.text}\n
                Hint: {e.msg}
        """
    
    explainer = CodeExplainer()
    explainer.visit(tree)
    return "This code:\n" + "\n".join(f"- {exp}" for exp in explainer.explanations)
