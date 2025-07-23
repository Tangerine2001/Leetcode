import importlib.util
import os
import json

test_cases = []

# Load test cases from test_cases.json
if os.path.exists('test_cases.json'):
    with open('test_cases.json') as json_file:
        test_cases = json.load(json_file)

# Iterate through solution_*.py files
for file in os.listdir('.'):
    if file.startswith('solution_') and file.endswith('.py'):
        print(f"Running: {file}")
        module_name = file[:-3]  # Strip .py
        spec = importlib.util.spec_from_file_location(module_name, file)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        # Make sure Solution class exists
        if hasattr(module, 'Solution'):
            sol = module.Solution()

            # Choose a method to call (e.g. 'solve')
            if hasattr(sol, 'minEatingSpeed'):
                for i, case in enumerate(test_cases):
                    try:
                        # Call the function with parsed input
                        input_args = case['input']
                        result = sol.minEatingSpeed(**input_args)
                        expected = case['output']

                        if result == expected:
                            print(f"Test case {i + 1} passed")
                        else:
                            print(f"Test case {i + 1} failed. Input: {input_args}. Got {result}, expected {expected}")
                    except Exception as e:
                        print(f"Test case {i+1} error: {e}")
            else:
                print(f"No 'solve' method in {file}")
        else:
            print(f"No Solution class in {file}")
