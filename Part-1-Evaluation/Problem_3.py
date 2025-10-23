"""
Problem 3 - From HumanEval/84: 

Given a positive integer N, return the total sum of its digits in binary.  
Example: 
For N = 1000, the sum of digits will be 1 the output should be "1". 

For N = 150, the sum of digits will be 6 the output should be "110". 

For N = 147, the sum of digits will be 12 the output should be "1100".  

Variables: @N integer 
Constraints: 0 ≤ N ≤ 10000. 
Output: a string of binary number. 
"""

#Prompting Strategy: Chain of Thought, LLM: OpenAI GPT 4.0
"""
Input: 
Think step-by-step to solve this problem then write the Python code to solve this problem 
[Pasted question here]

Output: 
Step-by-step reasoning
The task is to compute the sum of the decimal digits of N (examples confirm this: 1000 → 1+0+0+0 = 1, 150 → 1+5+0 = 6, etc.).
After computing that decimal-digit sum (call it total), convert total to its binary representation and return that as a string (no 0b prefix).
Edge cases:
If N == 0, the digit-sum is 0 and the binary string is "0".
Input is expected to be an integer 0 ≤ N ≤ 10000; the function checks for an integer and non-negativity.

[Generated code is given below]
"""
def solution1(N):
    if not isinstance(N, int):
        raise TypeError("N must be an integer")
    if N < 0:
        raise ValueError("N must be non-negative")
    
    total = 0
    n = N
    if n == 0:
        total = 0
    else:
        while n > 0:
            total += n % 10
            n //= 10
    
    return format(total, 'b')


#Prompting Strategy: Self Planning, LLM: GPT: 4.0
"""
Input:  
Before writing code, outline a plan that describes what functions you will implement and how they will interact. 
Then, based on your plan, write a python code for this problem
[Pasted question here]

Output:
🧠 Step 1: Problem Understanding
You're given a positive integer N (where 0 ≤ N ≤ 10000).
You need to:
Find the sum of its digits.
Convert that sum into binary.
Return the binary representation as a string.
✅ Example Walkthroughs
Input	Digits	Sum	Binary Output
1000	1 + 0 + 0 + 0	1	"1"
150	1 + 5 + 0	6	"110"
147	1 + 4 + 7	12	"1100"

🧩 Step 2: Plan / Function Design
Function 1: solve(N)
Purpose:
Given integer N, returns a binary string representing the sum of its digits.
Steps:
Convert the integer N to a string to easily iterate over each digit.
Compute sum of digits:
Use a loop or comprehension to convert each character to int and sum them.
Example: sum(int(digit) for digit in str(N))
Convert the sum to binary:
Use Python's built-in bin() function, which gives a string like '0b110'.
Slice off the '0b' prefix using [2:].
Return the resulting binary string.

⚙️ Step 3: Function Interaction
There's only one function:
solve(N) — performs both digit summation and binary conversion.
No helper functions are required for this simple transformation, but the process is modular enough that they could be added if needed. 

[Generated code is given below]
"""

def solution2(N): 
    digit_sum = sum(int(digit) for digit in str(N))
    
    binary_representation = bin(digit_sum)[2:]
    
    return binary_representation

#Prompting Strategy: Chain of Thought, LLM: Claude Sonnet 4.5
"""
Input: 
Think step-by-step to solve this problem then write the Python code to solve this problem 
[Pasted question here]

Output:
Step-by-Step Reasoning:

Understand the problem:

Take a positive integer N
Calculate the sum of its digits
Convert that sum to binary
Return the binary representation as a string

Verify with examples:

N = 1000:
Digits: 1, 0, 0, 0
Sum: 1 + 0 + 0 + 0 = 1
Binary of 1: "1" ✓


N = 150:
Digits: 1, 5, 0
Sum: 1 + 5 + 0 = 6
Binary of 6: "110" ✓


N = 147:
Digits: 1, 4, 7
Sum: 1 + 4 + 7 = 12
Binary of 12: "1100" ✓


Algorithm:

Convert the integer to a string to access individual digits
Sum all the digits
Convert the sum to binary using Python's bin() function
Remove the '0b' prefix from the binary string
Return the result


Edge cases:

N = 0 → sum = 0 → binary = "0"
Single digit numbers
Maximum constraint (N = 10000)

[Generate code is given below]
"""

def solution3(N):
    digit_sum = sum(int(digit) for digit in str(N))
    
    binary_result = bin(digit_sum)[2:]
    
    return binary_result

#Prompting Strategy: Self Planning, LLM: Claude Sonnet 4.5
"""
Input:  
Before writing code, outline a plan that describes what functions you will implement and how they will interact. 
Then, based on your plan, write a python code for this problem
[Pasted question here]

Output: 
Plan
I'll create a solution with the following approach:Functions to Implement:
solve(N) - Main function that:

Takes a positive integer N as input
Calculates the sum of all digits in N
Converts the sum to binary representation
Returns the binary as a string (without '0b' prefix)


Algorithm Flow:
Convert N to a string to access individual digits
Iterate through each digit character and convert it back to integer
Sum all the digits
Convert the sum to binary using Python's bin() function
Remove the '0b' prefix from the binary string
Return the binary string
Key Considerations:

bin() function returns a string like '0b1100', need to strip '0b'
Sum of digits: for 1000 → 1+0+0+0 = 1
Sum of digits: for 150 → 1+5+0 = 6, and 6 in binary is '110'
Sum of digits: for 147 → 1+4+7 = 12, and 12 in binary is '1100'
Handle edge case: N = 0 should return "0"
Verification with Examples:

N = 1000: digits sum = 1 → binary = "1" ✓
N = 150: digits sum = 6 → binary = "110" (6 = 4+2) ✓
N = 147: digits sum = 12 → binary = "1100" (12 = 8+4) ✓

[Generated code is given below]
"""
def solution4(N): 
    digit_sum = sum(int(digit) for digit in str(N))
    
    binary_result = bin(digit_sum)[2:]
    
    return binary_result


#Solution: 
def solve(N): 
    return bin(sum(int(i) for i in str(N)))[2:]
        
#Test Cases: 
def check(candidate):  
    # Check some simple cases 
    assert True, "This prints if this assert fails 1 (good for debugging!)" 
    assert candidate(1000) == "1", "Error" 
    assert candidate(150) == "110", "Error" 
    assert candidate(147) == "1100", "Error"  
    
    # Check some edge cases that are easy to work out by hand. 
    assert True, "This prints if this assert fails 2 (also good for debugging!)" 
    assert candidate(333) == "1001", "Error" 
    assert candidate(963) == "10010", "Error"

if __name__ == "__main__":
    check(solution1)
    print("All tests passed for Solution 1!")
    check(solution2)
    print("All tests passed for Solution 2!")
    check(solution3)
    print("All tests passed for Solution 3!")
    check(solution4)
    print("All tests passed for Solution 4!")