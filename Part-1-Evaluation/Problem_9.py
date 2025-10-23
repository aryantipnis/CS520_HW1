"""
Problem 9 - From CodeScore-MBPP-ET:
Write a function to find t-nth term of geometric series.

"""

#Prompting Strategy: Chain of Thought, LLM: OpenAI GPT 4.0
"""
Input: 
Think step-by-step to solve this problem then write the Python code to solve this problem 
[Pasted question here]

Output: 
Step-by-step reasoning
A geometric series (sequence) is defined by a first term a and a common ratio r.
The terms are: a, a*r, a*r^2, a*r^3, ....
The t-th term (1-based indexing) is a * r^(t-1).
Requirements to decide:
We should treat t (or n) as a positive integer. If t <= 0 it's not valid for the usual definition — raise an error.
Allow a and r to be any numeric types (ints or floats). Use exponentiation with an integer exponent.
For large t the result may be very large (overflow/very big integer or very large float); that's expected unless you ask for modular arithmetic or arbitrary precision handling beyond Python’s defaults.
Implementation: validate t, then return a * (r ** (t-1)). Use pow(r, t-1) (same effect).


[Generated code is given below]
"""
import math

def solution1(a, t, r):
    if not isinstance(t, int):
        raise TypeError("t must be an integer (1-based index)")
    if t < 1:
        raise ValueError("t must be >= 1")
    return a * (math.pow(r, t - 1))


#Prompting Strategy: Self Planning, LLM: GPT: 4.0
"""
Input:  
Before writing code, outline a plan that describes what functions you will implement and how they will interact. 
Then, based on your plan, write a python code for this problem
[Pasted question here]

Output: 
🧩 Plan
Step 1: Understand the problem
We are asked to find the t-th term of a geometric series.
A geometric series has the form:
a, a·r, a·r², a·r³, …
where
a = first term
r = common ratio
t = term number (1-indexed)
 
Step 2: Define the function
We'll define a single function:
def geometric_term(a, r, t):
Parameters:
a: first term of the series
r: common ratio
t: the term position (1-indexed)
Returns:
The t-th term of the series (an integer or float depending on inputs).
Step 3: Compute the t-th term
We simply apply the formula:
term = a * (r ** (t - 1))
Step 4: Return the result
Return the computed term.
Step 5: Example Tests
geometric_term(2, 3, 4) → 2 * 3³ = 54
geometric_term(3, 2, 5) → 3 * 2⁴ = 48
geometric_term(5, 1, 10) → 5 * 1⁹ = 5

[Generated code is given below]
"""

def solution2(a, t, r): 
    term = a * (r ** (t - 1))
    return term

#Prompting Strategy: Chain of Thought, LLM: Claude Sonnet 4.5
"""
Input: 
Think step-by-step to solve this problem then write the Python code to solve this problem 
[Pasted question here]

Output:
Step-by-Step Reasoning:

Understand geometric series:

A geometric series has a constant ratio between consecutive terms
General form: a, ar, ar², ar³, ar⁴, ...
Where:

a = first term
r = common ratio
n = term number (starting from 1)

Formula for nth term:

The nth term of a geometric series is: T_n = a x r^(n-1)
Examples:

1st term: a x r^0 = a
2nd term: a x r^1 = ar
3rd term: a x r^2 = ar²
nth term: a x r^(n-1)


Verify with examples:

Series: 2, 6, 18, 54, ... (a=2, r=3)

1st term: 2 x 3^0 = 2 x 1 = 2 ✓
2nd term: 2 x 3^1 = 2 x 3 = 6 ✓
3rd term: 2 x 3^2 = 2 x 9 = 18 ✓
4th term: 2 x 3^3 = 2 x 27 = 54 ✓


Series: 5, 10, 20, 40, ... (a=5, r=2)

1st term: 5 x 2^0 = 5 ✓
4th term: 5 x 2^3 = 5 x 8 = 40 ✓

Edge cases:

n = 1: Should return a (first term)
r = 0: All terms after first become 0
r = 1: All terms equal to a
r < 0: Alternating series
n ≤ 0: Invalid input


Implementation considerations:

Use the power operator ** or pow() function
Handle floating-point ratios
Validate inputs

[Generate code is given below]
"""

def solution3(a, n, r):
    if n <= 0:
        raise ValueError("Term number n must be positive (n >= 1)")
    
    nth_term = a * (r ** (n - 1))
    
    return nth_term

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
A geometric series (or geometric progression) is a sequence where each term after the first is found by multiplying the previous term by a constant called the common ratio (r).
General form: a, ar, ar², ar³, ar⁴, ...
Where:

a = first term
r = common ratio
n = term number (1-indexed or 0-indexed)

The nth term formula: T_n = a x r^(n-1) (for 1-indexed)
Examples:

Series: 2, 6, 18, 54, ... (a=2, r=3)

T₁ = 2
T₂ = 6
T₃ = 18
T₄ = 54
T_n = 2 x 3^(n-1)


Series: 1, 0.5, 0.25, 0.125, ... (a=1, r=0.5)

T_n = 1 x 0.5^(n-1)

Functions to Implement:

geometric_term(a, r, n) - Main function that:

Takes first term a, common ratio r, and term position n
Calculates the nth term using the formula
Returns the nth term value

Algorithm Flow:
Main Function:

Validate inputs (n should be positive)
Apply formula: nth_term = a x r^(n-1)
Return the result

Alternative Iterative Approach:

Start with first term a
Multiply by r for (n-1) times
Return the result

Key Considerations:

Handle edge cases: n=1, r=0, r=1, negative r
Use ** operator or pow() for exponentiation
Consider floating point precision for decimal ratios
Decide on indexing: 1-indexed (T₁ is first term) or 0-indexed

Formula:

nth term (1-indexed): T_n = a x r^(n-1)
nth term (0-indexed): T_n = a x r^n

I'll use 1-indexed (more common in mathematics).
Now, let me implement this:

[Generated code is given below]
"""
def solution4(a, n, r): 
    if n < 1:
        raise ValueError("Term position n must be >= 1")
    
    nth_term = a * (r ** (n - 1))
    
    return nth_term

#Solution: 
def tn_gp(a,n,r):
    tn = a * (math.pow(r, n - 1))
    return tn
        
#Test Cases: 
def check(candidate):
    assert candidate(1,5,2)==16
    assert candidate(1,5,4)==256
    assert candidate(2,6,3)==486
    assert candidate(3,9,6)==5038848.0
    assert candidate(4,4,2)==32.0
    assert candidate(2,5,4)==512.0
    assert candidate(2,8,5)==156250.0
    assert candidate(1,9,7)==5764801.0
    assert candidate(2,9,5)==781250.0
    assert candidate(4,9,5)==1562500.0
    assert candidate(1,10,4)==262144.0
    assert candidate(3,5,5)==1875.0
    assert candidate(3,3,6)==108.0
    assert candidate(2,8,6)==559872.0
    assert candidate(3,3,3)==27.0
    assert candidate(4,2,6)==24.0
    assert candidate(1,3,5)==25.0
    assert candidate(5,3,3)==45.0
    assert candidate(3,1,4)==3.0
    assert candidate(1,3,4)==16.0
    assert candidate(3,4,6)==648.0
    assert candidate(4,3,1)==4.0
    assert candidate(4,5,4)==1024.0
    assert candidate(3,8,6)==839808.0
    assert candidate(1,5,5)==625.0
    assert candidate(3,10,2)==1536.0
    assert candidate(1,3,3)==9.0
    assert candidate(2,7,5)==31250.0
    assert candidate(1,1,4)==1.0
    assert candidate(5,8,1)==5.0
    assert candidate(5,2,3)==15.0
    assert candidate(4,6,2)==128.0
    assert candidate(4,9,5)==1562500.0
    assert candidate(5,9,2)==1280.0
    assert candidate(3,7,6)==139968.0
    assert candidate(3,6,3)==729.0
    assert candidate(4,3,2)==16.0
    assert candidate(3,5,8)==12288.0
    assert candidate(6,3,7)==294.0
    assert candidate(1,9,6)==1679616.0
    assert candidate(2,2,7)==14.0
    assert candidate(1,8,6)==279936.0
    assert candidate(1,10,3)==19683.0
    assert candidate(4,5,3)==324.0
    assert candidate(6,9,3)==39366.0
    assert candidate(6,1,8)==6.0
    assert candidate(6,7,6)==279936.0
    assert candidate(3,2,1)==3.0
    assert candidate(6,3,6)==216.0
    assert candidate(3,4,5)==375.0
    assert candidate(5,4,2)==40.0
    assert candidate(1,3,4)==16.0
    assert candidate(1,9,4)==65536.0
    assert candidate(3,10,7)==121060821.0
    assert candidate(6,5,6)==7776.0
    assert candidate(4,2,4)==16.0
    assert candidate(4,9,3)==26244.0
    assert candidate(5,4,3)==135.0
    assert candidate(2,5,5)==1250.0
    assert candidate(1,10,1)==1.0
    assert candidate(4,4,3)==108.0
    assert candidate(5,2,1)==5.0
    assert candidate(4,6,8)==131072.0
    assert candidate(3,2,9)==27.0
    assert candidate(5,10,5)==9765625.0
    assert candidate(1,2,3)==3.0
    assert candidate(1,4,9)==729.0
    assert candidate(2,8,5)==156250.0
    assert candidate(6,2,2)==12.0
    assert candidate(6,7,7)==705894.0
    assert candidate(2,11,6)==120932352.0
    assert candidate(4,8,8)==8388608.0
    assert candidate(6,10,8)==805306368.0
    assert candidate(3,3,2)==12.0
    assert candidate(6,7,7)==705894.0
    assert candidate(1,4,2)==8.0
    assert candidate(1,8,8)==2097152.0
    assert candidate(2,7,7)==235298.0
    assert candidate(6,3,8)==384.0
    assert candidate(2,5,3)==162.0
    assert candidate(4,4,8)==2048.0
    assert candidate(5,8,4)==81920.0
    assert candidate(2,1,7)==2.0
    assert candidate(5,3,4)==80.0
    assert candidate(2,5,4)==512.0
    assert candidate(4,11,3)==236196.0
    assert candidate(6,8,6)==1679616.0
    assert candidate(7,7,2)==448.0
    assert candidate(6,4,2)==48.0
    assert candidate(4,1,3)==4.0
    assert candidate(5,10,5)==9765625.0
    assert candidate(5,11,2)==5120.0
    assert candidate(4,4,4)==256.0
    assert candidate(4,9,1)==4.0
    assert candidate(6,5,5)==3750.0
    assert candidate(7,5,6)==9072.0
    assert candidate(4,4,8)==2048.0
    assert candidate(1,3,1)==1.0
    assert candidate(2,10,5)==3906250.0
    assert candidate(6,9,4)==393216.0
    assert candidate(3,4,8)==1536.0
    assert candidate(7,4,6)==1512.0


if __name__ == "__main__":
    check(tn_gp)
    print("Solution passed!")
    check(solution1)
    print("All tests passed for Solution 1!")
    check(solution2)
    print("All tests passed for Solution 2!")
    check(solution3)
    print("All tests passed for Solution 3!")
    check(solution4)
    print("All tests passed for Solution 4!")