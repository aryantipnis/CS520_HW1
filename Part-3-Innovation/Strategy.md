## Part 3: Innovation — Proposed Strategy

## Overview
In this section, we propose and evaluate a multi-step prompting strategy designed to improve LLM performance on programming tasks where prior approaches in Part 1 failed.  
The goal is to enhance reasoning consistency, error correction, and robustness across different model families.

## Idea 
Combine **stepwise planning + coding + unit-test-driven refinement + counterexample search** using role-based prompts (Planner, Tester, Coder, Debugger, Counterexample Search) to force reasoning, generate tests first, and iteratively repair until correct.

## Why this strategy?
- Forces the model to **think before coding** (Planner).
- Produces **unit tests up front** so the model must satisfy explicit edge cases rather than guessing.
- Provides a tight **feedback loop**: failing tests produce concrete, actionable failure reports for the model to fix.
- Uses **counterexample search** (enumeration or randomized sampling) to find gaps beyond the supplied tests, preventing overfitting to the initial suite.
- Role separation (Planner/Tester/Coder/Debugger) reduces the model’s tendency to jump to a familiar template and encourages structured reasoning.

## Workflow: 
1. Step by Step Planning (Planner): Prompt the LLM to produce:
    - Brief plan of approach
    - Invariants/constraints to maintain
    - Key edge cases to test

2. Test Generation (Tester): prompt the LLM to write unit tests 

3. Code Generation (Coder): prompt to write code implementing the plan and the tests.

4. Run Tests: execute tests. Capture failing tests if any. 

5. Refinement: feed failing tests and failure logs back to LLM with an explanation of the failing test case. Repeat this step until the generated code passes all test cases.  

6. Counterexample Search: run enumerative or randomized inputs to discover further edge cases; if found, go to step 5.

## Prompts

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

## Testing Plan 

1. **Select Targets**
   - Use the *failed problems* from Part 2 (e.g., Problem 7 and Problem 10).

2. **Choose LLMs (two different families)**
   - We choose OpenAI GPT-4 and Claude Sonnet 4.5 for consistency.

3. **Run Procedure per (problem, model) pair**
   - Call Planner - get plan + edge cases  
   - Call Tester - get unit tests  
   - Call Coder - get code  
   - Execute tests locally  
   - If failures, call Debugger with structured failure report, get patched code, repeat  
   - After passing supplied tests, run Counterexample Search. If counterexample found, return to Debugger.  
   - Save all intermediate artifacts (prompts, generated tests, generated code versions, test logs, counterexamples).

4. **Repeat**
   - Run the above 3 times per model per problem to measure stability and variance.
   - Note: A sample run is given in the files `ProblemX_LLM.md`

## Evaluation Metrics

- **Pass@k**: Does the final single candidate (after refinement) pass all the tests?
- **Iterations to Convergence**: Number of debug cycles needed until tests pass.







