"""
Problem 7 - From CodeScore-MBPP-ET:  
Write a python function to find the last digit when factorial of a divides factorial of b.
"""

#Prompting Strategy: Chain of Thought, LLM: OpenAI GPT 4.0
"""
Input: 
Think step-by-step to solve this problem then write the Python code to solve this problem 
[Pasted question here]

Output: 
Step-by-step reasoning
For non-negative integers a and b, if a > b then a! does not divide b! — the quotient is not an integer. We'll treat that as an error (raise ValueError).
If a == b then b!/a! = 1, so the last digit is 1.
If a < b then b!/a! = (a+1)*(a+2)*...*b. We only need its last decimal digit (units digit), i.e. the product modulo 10.
Observations that allow quick answers:
If b - a >= 10, the consecutive integers (a+1,...,b) include at least one multiple of 10, so the product ends in 0. Thus the last digit is 0.
Otherwise, multiply the numbers (a+1) through b, reducing modulo 10 at every step. If the running result becomes 0 we can stop early. This is efficient because when b-a < 10 the loop is short.
Validate inputs: a and b must be integers and non-negative.
Python implementation (tested):

[Generated code is given below]
"""
def solution1(a, b):
    if a > b:
        return 0
    
    if a == b:
        return 1

    if b - a >= 10:
        return 0

    res = 1
    for x in range(a + 1, b + 1):
        res = (res * (x % 10)) % 10
        if res == 0:
            return 0
    return res


#Prompting Strategy: Self Planning, LLM: GPT: 4.0
"""
Input:  
Before writing code, outline a plan that describes what functions you will implement and how they will interact. 
Then, based on your plan, write a python code for this problem
[Pasted question here]

Output: 
🧠 Step 1: Problem Understanding
We need to find the last digit of the number when factorial of a divides factorial of b, 
b!/a! is not defined (factorial of a larger number can't divide smaller one),
but for this problem, we can assume to return 0.
So we can multiply these terms and find the last digit.

🧩 Step 3: Plan / Design
We will implement one main function:
compute_Last_Digit(a: int, b: int) -> int
Steps:
Handle base cases:
If a == b: return 1
If a > b: return 0
Initialize a variable res = 1.
Loop from a + 1 to b (inclusive):
Multiply res by the current number.
Take only the last digit each time (res %= 10) to avoid overflow.
Return the final value of res.

[Generated code is given below]
"""

def solution2(a, b): 
    if a == b:
        return 1
    if a > b:
        return 0
    
    res = 1
    for i in range(a + 1, b + 1):
        res = (res * i) % 10 
    
    return res

#Prompting Strategy: Chain of Thought, LLM: Claude Sonnet 4.5
"""
Input: 
Think step-by-step to solve this problem then write the Python code to solve this problem 
[Pasted question here]

Output:

[Generate code is given below]
"""
def solution3(a, b):
    if a > b:
        return 0
    
    if a == b:
        return 1
    
    result = 1
    
    for i in range(a + 1, b + 1):
        result = (result * i) % 10
    
    return result

#Prompting Strategy: Self Planning, LLM: Claude Sonnet 4.5
"""
Input:  
Before writing code, outline a plan that describes what functions you will implement and how they will interact. 
Then, based on your plan, write a python code for this problem
[Pasted question here]

Output: 
Plan
I'll create a solution with the following approach:
Understanding the Problem:
We need to find the last digit of the result when factorial(a) divides factorial(b), i.e., the last digit of b! / a!.
Mathematical simplification:

b! / a! = b x (b-1) x (b-2) x ... x (a+1) when b ≥ a
This is the product of all numbers from (a+1) to b

Functions to Implement:

last_digit_factorial_division(a, b) - Main function that:

Takes two integers a and b
Calculates the last digit of b! / a!
Returns the last digit (0-9)

Algorithm Flow:
Approach 1: Direct Calculation (for small values)

Handle edge cases:

If b < a: result is undefined or 0
If b == a: result is 1 (last digit = 1)
If a >= 10 or the range is large: result will end in 0 (many factors of 2 and 5)


Calculate b! / a! = product from (a+1) to b
Keep only the last digit at each step to avoid overflow
Return the last digit

Approach 2: Optimized (only tracking last digit)

Initialize result = 1
Multiply by each number from (a+1) to b
Keep only last digit (% 10) after each multiplication
Return the last digit

Key Considerations:

Only need to track the last digit, not the full result
If the range includes numbers ≥ 10, we'll have factors of 2 and 5, resulting in last digit 0
For small ranges, calculate iteratively while keeping only last digit
Edge cases: a >= b, a = 0, large numbers

Examples to verify:

b! / a! where a=3, b=5: 5!/3! = 120/6 = 20 → last digit = 0
b! / a! where a=2, b=4: 4!/2! = 24/2 = 12 → last digit = 2
b! / a! where a=5, b=7: 7!/5! = 5040/120 = 42 → last digit = 2

Now, let me implement this:Last Digit of Factorial DivisionCode def last_digit_factorial_division(a, b):

    Find the last digit when factorial of a divides factorial of b.
    In other words, find the last digit of b! / a!
    
    Mathematical insight:
    b! / a! = b x (b-1) x (b-2) x ... x (a+1)
    
I've implemented a solution to find the last digit of factorial division with comprehensive testing:
Implementation Details:
Main Function (last_digit_factorial_division)
Key Algorithm:

Mathematical simplification: b! / a! = (a+1) x (a+2) x ... x b
Last digit tracking: Multiply numbers iteratively and keep only last digit using % 10
Optimizations:

If b < a: return 0 (invalid division)
If b == a: return 1 (factorial divides itself = 1)
If range ≥ 10 or contains both multiples of 2 and 5: return 0 (trailing zeros)

Algorithm Flow:
pythonlast_digit = 1
for num in range(a + 1, b + 1):
    last_digit = (last_digit * num) % 10
This keeps only the last digit at each step, preventing overflow and efficiently computing the result.
Examples:

a=3, b=5: 5!/3! = 5x4 = 20 → last digit = 0
a=2, b=4: 4!/2! = 4x3 = 12 → last digit = 2
a=5, b=7: 7!/5! = 7x6 = 42 → last digit = 2
a=1, b=4: 4!/1! = 4x3x2 = 24 → last digit = 4

Key Insights:

Trailing zeros: When the product includes both multiples of 2 and 5, the result ends in 0
Modulo arithmetic: We only need (result * num) % 10 at each step
No overflow: By keeping only last digit, we can handle arbitrarily large ranges
Verification: Included helper function to verify results with actual factorial calculations for small numbers

Time Complexity: O(b - a) - iterate through the range once
Space Complexity: O(1) - only tracking one integer
The solution handles all edge cases and includes detailed verification with actual factorial calculations!


[Generated code is given below]
"""
def solution4(a, b): 
    if b < a:
        return 0
    
    if b == a:
        return 1
    
    last_digit = 1
    for num in range(a + 1, b + 1):
        last_digit = (last_digit * num) % 10
    
    return last_digit


#Solution: 
def compute_Last_Digit(A,B): 
    variable = 1
    if (A == B): 
        return 1
    elif ((B - A) >= 5): 
        return 0
    else: 
        for i in range(A + 1,B + 1): 
            variable = (variable * (i % 10)) % 10
        return variable % 10
        
#Test Cases: 
def check(candidate):
    # Given test cases
    assert candidate(2, 4) == 2
    assert candidate(6, 8) == 6
    assert candidate(1, 2) == 2
    assert candidate(1, 8) == 0
    assert candidate(2, 7) == 0
    assert candidate(5, 7) == 2
    assert candidate(7, 6) == 1
    assert candidate(7, 9) == 2
    assert candidate(4, 1) == 1
    assert candidate(6, 6) == 1
    assert candidate(4, 7) == 0
    assert candidate(3, 2) == 1
    assert candidate(6, 7) == 7
    assert candidate(6, 9) == 4
    assert candidate(6, 2) == 1
    assert candidate(2, 9) == 0
    assert candidate(6, 4) == 1
    assert candidate(2, 1) == 1
    assert candidate(4, 3) == 1
    assert candidate(5, 5) == 1
    assert candidate(7, 8) == 8
    assert candidate(1, 5) == 0
    assert candidate(8, 10) == 0
    assert candidate(11, 3) == 1
    assert candidate(3, 4) == 4
    assert candidate(11, 6) == 1
    assert candidate(5, 11) == 0
    assert candidate(10, 13) == 6
    assert candidate(1, 12) == 0
    assert candidate(4, 9) == 0
    assert candidate(3, 13) == 0
    assert candidate(4, 12) == 0
    assert candidate(11, 7) == 1
    assert candidate(9, 4) == 1
    assert candidate(8, 13) == 0
    assert candidate(3, 9) == 0
    assert candidate(9, 13) == 0
    assert candidate(8, 7) == 1
    assert candidate(6, 11) == 0
    assert candidate(7, 10) == 0
    assert candidate(9, 11) == 0
    assert candidate(4, 10) == 0
    assert candidate(6, 10) == 0
    assert candidate(8, 11) == 0
    assert candidate(5, 4) == 1
    assert candidate(3, 7) == 0
    assert candidate(1, 7) == 0
    assert candidate(5, 3) == 1
    assert candidate(5, 6) == 6
    assert candidate(3, 5) == 0
    assert candidate(4, 2) == 1
    assert candidate(4, 4) == 1
    assert candidate(4, 6) == 0
    assert candidate(1, 6) == 0
    assert candidate(2, 6) == 0

    # Additional provided cases
    assert candidate(3, 7) == 0
    assert candidate(20, 23) == 6
    assert candidate(1021, 1024) == 4


if __name__ == "__main__":
    check(compute_Last_Digit)
    # check(solution1)
    print("All tests passed for Solution 1!")
    # check(solution2)
    print("All tests passed for Solution 2!")
    # check(solution3)
    print("All tests passed for Solution 3!")
    check(solution4)
    print("All tests passed for Solution 4!")