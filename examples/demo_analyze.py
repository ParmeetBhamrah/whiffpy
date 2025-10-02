from whiffpy import analyze

code = '''while True:
            print("Psb")
        '''

result = analyze(code)

print("EXPLANATION:\n", result["explanation"])
print("OUTPUT:\n", result["output"])
print("ANALYSIS:\n", result["error_analysis"])
print("ERROR:\n", result["error"])