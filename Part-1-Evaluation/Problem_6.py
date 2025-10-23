"""
Problem 6 - From CodeScore-MBPP-ET: 

Write a python function to find the minimum number of rotations required to get the same string.
"""

#Prompting Strategy: Chain of Thought, LLM: OpenAI GPT 4.0
"""
Input: 
Think step-by-step to solve this problem then write the Python code to solve this problem 
[Pasted question here]

Output: 
Plan (step-by-step)
If input string s is empty, return 0 because no positive rotation needed (or possible).
Let n = len(s). Rotating left by k (where 1 <= k <= n) produces s[k:] + s[:k].
Check k from 1 through n and return the first k where the rotated string equals s.
Rotation by n always returns the original string, so the loop will always find a k and return by n at the latest.
This is simple and correct; worst-case time is O(n^2) for an n-length string (sufficient for typical problem sizes).
If you want a faster algorithm, we can compute the minimal rotation period using string-search techniques (e.g., KMP on s + s) to reduce to O(n).
Python implementation (tested above):


[Generated code is given below]
"""
def solution1(s):
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    
    n = len(s)
    if n == 0:
        return 0
    for k in range(1, n + 1):
        if s[k:] + s[:k] == s:
            return k
    return n

#Prompting Strategy: Self Planning, LLM: GPT: 4.0
"""
Input:  
Before writing code, outline a plan that describes what functions you will implement and how they will interact. 
Then, based on your plan, write a python code for this problem
[Pasted question here]

Output: 
We need to find the minimum number of rotations required to obtain the same string again.
For example:
"aaaa" → All characters are the same → only 1 rotation gives the same string.
"ab" → Rotate once → "ba" (not same), rotate again → "ab" (same).
✅ Minimum rotations = 2
We're looking for the smallest positive integer k (1 ≤ k ≤ len(s)) such that:
rotating the string k times = original string
If no smaller rotation works, then the answer is the string's length.

🧩 Step 2: Plan / Design
We'll define one function:
find_Rotations(s: str) -> int
Plan:
Handle edge case: If s is empty → return 0 (no rotations needed).
Iterate over all rotation amounts k from 1 to len(s):
Rotate string by k positions.
Check if rotated string equals original.
If yes, return k (that's the minimum rotation).
If no such rotation found, return len(s) (because it repeats only after full rotation).
Helper Concept:
Rotation of string by k:
rotated = s[k:] + s[:k]

[Generated code is given below]
"""

def solution2(s): 
    if not s:  
        return 0
    
    n = len(s)
    for k in range(1, n + 1):
        rotated = s[k:] + s[:k]
        if rotated == s:
            return k
    return n

#Prompting Strategy: Chain of Thought, LLM: Claude Sonnet 4.5
"""
Input: 
Think step-by-step to solve this problem then write the Python code to solve this problem 
[Pasted question here]

Output:
Step-by-Step Reasoning:
Understand the problem:

Given a string, we need to find the minimum number of rotations to get back to the same string
A rotation means moving characters from the beginning to the end (or vice versa)
Example: "abc" → "bca" → "cab" → "abc" (3 rotations to return)

Key insight:

If a string has a repeating pattern, it will return to itself before completing a full rotation cycle
Example: "abab" → "baba" → "abab" (2 rotations, not 4)
Example: "aaaa" → "aaaa" (1 rotation)
Example: "abc" → "bca" → "cab" → "abc" (3 rotations)

Mathematical approach:

The minimum number of rotations is related to the string's period
The answer is: len(string) / period_length
Where period_length is the length of the smallest repeating unit

Algorithm:

Check each rotation from 1 to len(string)
For each rotation, check if we get back the original string
Return the first (minimum) rotation count that gives us the original string

Examples to verify:

"abc": Need 3 rotations (abc → bca → cab → abc)
"abab": Need 2 rotations (abab → baba → abab)
"aaa": Need 1 rotation (aaa → aaa)
"abcd": Need 4 rotations
"" (empty): Need 0 rotations

[Generate code is given below]
"""

def solution3(s):
    if len(s) == 0:
        return 0
    
    if len(s) == 1:
        return 1
    
    doubled = s + s
    
    for i in range(1, len(s) + 1):
        if doubled[i:i + len(s)] == s:
            return i
    
    return len(s)

#Prompting Strategy: Self Planning, LLM: Claude Sonnet 4.5
"""
Input:  
Before writing code, outline a plan that describes what functions you will implement and how they will interact. 
Then, based on your plan, write a python code for this problem
[Pasted question here]

Output: 
PlanI'll create a solution with the following approach:Functions to Implement:
min_rotations(s) - Main function that:

Takes a string as input
Finds the minimum number of rotations needed to get back to the original string
Returns the minimum rotation count


Understanding the Problem:A rotation of a string means moving characters from the beginning to the end:

"abc" → "bca" (1 rotation)
"bca" → "cab" (2 rotations)
"cab" → "abc" (3 rotations, back to original)
The minimum number of rotations to get the same string is related to the period of the string (the smallest repeating pattern).Examples:

"abc" → needs 3 rotations (no repeating pattern)
"abab" → needs 2 rotations ("ab" repeats)
"aaa" → needs 1 rotation (all same character)
"abcabc" → needs 3 rotations ("abc" repeats)
Algorithm Flow:Approach 1: Brute Force

Start with rotation count = 1
Rotate the string and compare with original
Keep rotating until we get back to the original string
Return the count
Approach 2: Mathematical/Pattern-based

The minimum rotations = length of string / length of smallest repeating unit
For a string of length n, the minimum rotations divide n evenly
We need to find the smallest divisor k such that rotating k times gives the original string
Key Considerations:

Empty string or single character → 1 rotation (or 0 depending on interpretation)
String with all same characters → 1 rotation
String length itself is always a valid answer (worst case)
The answer must be a divisor of the string length
Algorithm Implementation:

Handle edge cases (empty or length 1)
Try all divisors of string length starting from 1
For each divisor k, check if rotating k positions gives the original string
Return the first (smallest) k that works
Now, let me implement this:

[Generated code is given below]
"""
def solution4(s): 
    if len(s) <= 1:
        return 1
    
    n = len(s)
    doubled = s + s
    
    for k in range(1, n + 1):
        if doubled[k:k + n] == s:
            return k
    
    return n


#Solution: 
def find_Rotations(str): 
    tmp = str + str
    n = len(str) 
    for i in range(1,n + 1): 
        substring = tmp[i: i+n] 
        if (str == substring): 
            return i 
    return n
        
#Test Cases: 
def check(candidate):
    assert candidate("aaaa") == 1
    assert candidate("ab") == 2
    assert candidate("abc") == 3
    assert candidate("kcwa") == 4
    assert candidate("ezxpedrz") == 8
    assert candidate("fgluxhtza") == 9
    assert candidate("mjoaexpfz") == 9
    assert candidate("linyxx") == 6
    assert candidate("pay") == 3
    assert candidate("rxmc") == 4
    assert candidate("qkkjahy") == 7
    assert candidate("slcswzxu") == 8
    assert candidate("zoiy") == 4
    assert candidate("rhjaux") == 6
    assert candidate("fkjfimi") == 7
    assert candidate("pbkflfnd") == 8
    assert candidate("rthqixv") == 7
    assert candidate("rej") == 3
    assert candidate("ifhbywu") == 7
    assert candidate("oost") == 4
    assert candidate("nxwjjwsas") == 9
    assert candidate("moockefg") == 8
    assert candidate("qqydevz") == 7
    assert candidate("wwivmp") == 6
    assert candidate("togvvenfp") == 9
    assert candidate("oolvpej") == 7
    assert candidate("tzegpv") == 6
    assert candidate("beahzutke") == 9
    assert candidate("xzwepkip") == 8
    assert candidate("sis") == 3
    assert candidate("qtbflguk") == 8
    assert candidate("jam") == 3
    assert candidate("gqbzuvv") == 7
    assert candidate("abvgipdym") == 9
    assert candidate("ttff") == 4
    assert candidate("jjeu") == 4
    assert candidate("rphw") == 4
    assert candidate("nbgwgz") == 6
    assert candidate("setbdn") == 6
    assert candidate("pscwbl") == 6
    assert candidate("flgboo") == 6
    assert candidate("bfxpdk") == 6
    assert candidate("mofei") == 5
    assert candidate("qyr") == 3
    assert candidate("uxk") == 3
    assert candidate("nbmy") == 4
    assert candidate("ege") == 3
    assert candidate("usoriq") == 6
    assert candidate("wjuwlt") == 6
    assert candidate("bnodui") == 6
    assert candidate("aevvqf") == 6
    assert candidate("iaktug") == 6
    assert candidate("vhufs") == 5
    assert candidate("hiat") == 4
    assert candidate("mzaym") == 5
    assert candidate("xnlqu") == 5
    assert candidate("zqdb") == 4
    assert candidate("flq") == 3
    assert candidate("oar") == 3
    assert candidate("fezfrb") == 6
    assert candidate("ipszr") == 5
    assert candidate("edyr") == 4
    assert candidate("nve") == 3
    assert candidate("yti") == 3
    assert candidate("bmfvr") == 5
    assert candidate("psafv") == 5
    assert candidate("zlhtd") == 5
    assert candidate("pacp") == 4
    assert candidate("qhgsk") == 5
    assert candidate("eyde") == 4
    assert candidate("eyv") == 3
    assert candidate("dxbgtvxq") == 8
    assert candidate("mfdx") == 4
    assert candidate("xask") == 4
    assert candidate("qddp") == 4
    assert candidate("oas") == 3
    assert candidate("fjilakl") == 7
    assert candidate("xwdsk") == 5
    assert candidate("owqgr") == 5
    assert candidate("lxv") == 3
    assert candidate("bxbb") == 4
    assert candidate("jbfisms") == 7
    assert candidate("zqupo") == 5
    assert candidate("qye") == 3
    assert candidate("hhxosqlg") == 8
    assert candidate("zhb") == 3
    assert candidate("iwkj") == 4
    assert candidate("maen") == 4
    assert candidate("lsliyhze") == 8
    assert candidate("doocsri") == 7
    assert candidate("cjc") == 3
    assert candidate("avi") == 3
    assert candidate("rfit") == 4
    assert candidate("tlgffvv") == 7
    assert candidate("vlk") == 3
    assert candidate("ljeftwkpr") == 9
    assert candidate("itzso") == 5
    assert candidate("zxfscko") == 7
    assert candidate("ewzfvb") == 6
    assert candidate("wdk") == 3
    assert candidate("gmlivxfm") == 8
    assert candidate("yvsnt") == 5

if __name__ == "__main__":
    check(solution1)
    print("All tests passed for Solution 1!")
    check(solution2)
    print("All tests passed for Solution 2!")
    check(solution3)
    print("All tests passed for Solution 3!")
    check(solution4)
    print("All tests passed for Solution 4!")