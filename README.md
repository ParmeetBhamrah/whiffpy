# WhiffPy 🐍💨  
**WhiffPy** is a smart Python code explainer and error analyzer designed for beginners, educators, and anyone who wants to understand Python code more deeply. It analyzes code, explains its structure in plain English, and provides actionable, friendly error messages.  

---

## 🚀 Features
- Beginner-friendly explanations of code structure using **Python's AST**  
- Human-readable **error analysis with suggestions** for common mistakes  
- **Safe code execution** with output and error capture  
- Flexible **CLI**: analyze files or code snippets, output as text or JSON, save results  
- Easy to extend: add new error hints or code patterns  

---

## 📦 Installation  

### Using pip (recommended for general usage)

WhiffPy **v0.1.2** is available on PyPI. You can install it directly with:

```sh
pip install whiffpy
````

After installation, run the CLI commands:

```sh
whiffpy path/to/file.py
```

### Using Poetry (for development)

Ensure you have **Python 3.9+** and [Poetry](https://python-poetry.org/) installed.

```sh
# Clone the repository and install dependencies
git clone https://github.com/ParmeetBhamrah/whiffpy.git
cd whiffpy
poetry install
```

---

## 🛠️ Usage

### Command Line Interface

Analyze a Python file:

```sh
whiffpy path/to/file.py
```

Analyze a code snippet directly:

```sh
whiffpy --code "print(1+1)"
```

Explain code structure only (no execution):

```sh
whiffpy path/to/file.py --explain-only
```

Output as JSON:

```sh
whiffpy path/to/file.py --json
```

Save output to a file:

```sh
whiffpy path/to/file.py --save result.txt
```

### Python API

```python
from whiffpy import analyze

code = "x = 1 / 0"
report = analyze(code)
print(report)
```

---

## 📁 Examples

Check the [`examples/`](examples) directory for demos:

* **examples/demo.py** → Basic code execution and error capture
* **examples/demo_analyze.py** → Full analysis with explanations

---

## 🧩 Development Notes

* **Add error hints** → edit `whiffpy/utils.py`
* **Extend code explanations** → edit `whiffpy/explainer.py`

---

## 📂 Project Structure

```
whiffpy/
│── __init__.py        # Main API (analyze)
│── cli.py             # Command-line interface
│── runner.py          # Code execution
│── explainer.py       # AST-based code explanations
│── error_analyzer.py  # Traceback parsing and suggestions
│── utils.py           # Error hints and result formatting
examples/              # Usage examples
README.md
pyproject.toml
poetry.lock
LICENSE
```

---

## 📄 License

WhiffPy is released under the **MIT License**.