## Revised Prompts: 

According to the new proposed multi-step strategy in Part 3, the prompts are: 

**Planner Prompt:**

"You are a planner. Problem: [Paste problem statement here].
1) Briefly (3–6 bullet points) outline the approach and the key constraint to maintain.*
2) List the 6 most important edge cases we must test.”

**Tester Prompt:**

“You are a Tester. Using the plan and edge cases from Planner, produce 10 unit tests in Python: a list of (input, expected_output). Include comments saying why each test matters.” 

**Coder Prompt:**

“You are a Coder. Implement the function `solution(args...)` described below. Use the plan and tests from Planner/Tester. Write clean, well-commented Python code and include the tests as a `if __name__ == "__main__":` block to run them.
Problem: [Paste problem statement here]
Return only the code file.”

**Debugger Prompt:**

“You are a Debugger. The following tests failed: [list failing tests]. Generate a code that takes into account this failing test case. [Explain why it failed]”


**Counter-example search Prompt:**

“Run this code over random inputs to find a counterexample that fails the test.”

If a counterexample is found, repeat the debugger step until the correct solution is found. 
