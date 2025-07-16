from whiffpy import analyze

code = '''
def greet_user(name):
    """Greets the user by name several times."""
    for i in range(3)
        print(f"Hello, {name}! Attempt {i+1}/3")

try:
    user_name = "World"
    greet_user(user_name)
    result = 10 / 0
except Exception as e:
    print("An error occurred:", e)
finally:
    print("Execution finished.")
'''

result = analyze(code)

print("EXPLANATION:\n", result["explanation"])
print("OUTPUT:\n", result["output"])
print("ANALYSIS:\n", result["error_analysis"])
print("ERROR:\n", result["error"])