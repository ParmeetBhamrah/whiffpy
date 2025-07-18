import argparse
import json
from whiffpy import analyze

def main():
    parser = argparse.ArgumentParser(
        description="WhiffPy - Analyze Python code with beginner-friendly explanations."
    )
    parser.add_argument("path", nargs="?", help="Path to a .py file containing code")
    parser.add_argument("--code", help="Direct code string to analyze")
    parser.add_argument("--explain-only", action="store_true", help="Only explain structure (no code execution)")
    parser.add_argument("--json", action="store_true", help="Output result as JSON")
    parser.add_argument("--save", help="Save output to a file")

    args = parser.parse_args()

    if args.code:
        code = args.code
    elif args.path:
        with open(args.path, 'r', encoding="utf-8") as f:
            code = f.read()
    else:
        print(" ! Provide either a file path or a code snippet using --code")
        return
    
    if args.explain_only:
        from whiffpy.explainer import explain_structure
        result = explain_structure(code)
        print(result)
        if args.save:
            with open(args.save, 'w', encoding="utf-8") as f:
                f.write(result)
        return
    
    report = analyze(code)

    if args.json:
        print(report.to_dict())
    else:
        print(report)

    if args.save:
        with open(args.save, "w", encoding="utf-8") as f:
            f.write(str(report))