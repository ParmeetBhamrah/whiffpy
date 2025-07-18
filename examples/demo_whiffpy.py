from whiffpy import analyze

# 📜 Sample code to test
sample_code = """
def find_max(numbers):
    max_val = numbers[0]
    for num in numbers:
        if num > max_val:
            max_val = num
    return max_val

def safe_divide(x, y):
    if y == 0:
        print("Cannot divide by zero")
        return None
    return x / y

values = [3, 7, 2, 9, 5]
largest = find_max(values)

result = safe_divide(largest, 0)

print("Largest number:", largest)
print("Division result:", result)
"""

report = analyze(sample_code)  # Returns a CodeReport object

print(report)