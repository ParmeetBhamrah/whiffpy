from whiffpy.runner import run_code

code = "print('Before error')\nx = 1 / 0"

result = run_code(code)

print("Output:", result["output"])
print("Error:", result["error"])