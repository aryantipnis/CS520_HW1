"""
Problem 1 - From HumanEval/68: 

Given an array representing a branch of a tree that has non-negative integer nodes your task 
is to pluck one of the nodes and return it. The plucked node should be the node with the 
smallest even value. If multiple nodes with the same smallest even value are found 
return the node that has smallest index.  The plucked node should be returned in a list, 
[ smalest_value, its index ], If there are no even values or the given array is empty, return [].  

Example 1:  Input: [4,2,3] Output: [2, 1] 
Explanation: 2 has the smallest even value, and 2 has the smallest index.  

Example 2: Input: [1,2,3] Output: [2, 1] 
Explanation: 2 has the smallest even value, and 2 has the smallest index.   

Example 3: Input: [] Output: []  

Example 4: Input: [5, 0, 3, 0, 4, 2] Output: [0, 1] 
Explanation: 0 is the smallest value, but there are two zeros, so we will choose the first zero, which has the smallest index.  

Constraints: * 1 <= nodes.length <= 10000 * 0 <= node.value 
"""

#Prompting Strategy: Chain of Thought, LLM: OpenAI GPT 4.0
"""
Input: 
Think step-by-step to solve this problem then write the Python code to solve this problem 
[Pasted question here]

Output: 
Nice — let's walk through it, then here's working Python you can run (I already ran it and included test outputs below).
Step-by-step reasoning
We scan the array left-to-right so that the first occurrence of any value is naturally preferred when values tie.
We only consider even numbers (v % 2 == 0).
Maintain min_even (the smallest even value found so far) and min_index (its index).
For each even v, update min_even and min_index only if min_even is None (no even seen yet) or v < min_even.
If v == min_even, do not update because the earlier index is preferred.
After the loop, if min_even is still None (no evens or empty array) return []; otherwise return [min_even, min_index].

[Generated code is given below]
"""
def solution1(arr):
    min_even = None
    min_index = -1

    for i, v in enumerate(arr):
        if v % 2 == 0:
            if min_even is None or v < min_even:
                min_even = v
                min_index = i

    return [] if min_even is None else [min_even, min_index]


#Prompting Strategy: Self Planning, LLM: GPT: 4.0
"""
Input:  
Before writing code, outline a plan that describes what functions you will implement and how they will interact. 
Then, based on your plan, write a python code for this problem
[Pasted question here]

Output: 
🧩 Step 1: Problem Understanding
    We are given an array of non-negative integers.
    We need to:
    Find the smallest even number in the array.
    If there are multiple occurrences, return the one with the smallest index.
    If there are no even numbers or the array is empty, return [].
    The result format should be [value, index].
🧠 Step 2: Plan / Design Outline
    We'll implement a clean, modular solution with clear logic flow.
    Function 1: find_smallest_even_node(arr)
    Purpose: Main function that returns [smallest_even_value, its_index] or [] if none found.
    Steps:
    Check if the array is empty → return [].
    Initialize:
    min_even = None
    min_index = -1
    Iterate through the array using enumerate(arr):
    Check if the number is even (num % 2 == 0).
    If it's the first even number found (min_even is None), set it as the current min.
    Otherwise, if it's smaller than min_even, update both min_even and min_index.
    After iteration:
    If min_even is still None, return [].
    Otherwise, return [min_even, min_index].
    Function 2: (Optional) is_even(num)
    Small helper function to improve readability (return num % 2 == 0).
🧩 Step 3: Function Interaction
    find_smallest_even_node() is the main function.
    It optionally uses is_even() to check parity.
    No other dependencies are needed — the code remains efficient (O(n) time, O(1) space).

    [Generated code is given below]
"""
def is_even(num):
    """Check if a number is even."""
    return num % 2 == 0

def solution2(arr): 
    if not arr:
        return []

    min_even = None
    min_index = -1

    for i, num in enumerate(arr):
        if is_even(num):
            if min_even is None or num < min_even:
                min_even = num
                min_index = i

    return [min_even, min_index] if min_even is not None else []


#Prompting Strategy: Chain of Thought, LLM: Claude Sonnet 4.5
"""
Input: 
Think step-by-step to solve this problem then write the Python code to solve this problem 
[Pasted question here]

Output:
I'll solve this step-by-step.
Step-by-Step Reasoning:

Understand the problem:

Find the smallest even value in the array
If there are multiple nodes with the same smallest even value, choose the one with the smallest index
Return [value, index]
Return [] if no even values exist or array is empty


Approach:

Iterate through the array
Track even values and their indices
Find the minimum even value
If multiple minimums exist, the first occurrence will naturally have the smallest index
Return the result in the required format


Edge cases:

Empty array → return []
No even values → return []
Multiple same smallest even values → return the first occurrence (smallest index)
Zero is even and is the smallest non-negative even number


Algorithm:

Iterate through array with index
Check if value is even (value % 2 == 0)
Track the smallest even value and its index
Return [smallest_even, index] or []

The solution works as follows:
Key Points:

Time Complexity: O(n) - single pass through the array
Space Complexity: O(1) - only storing two variables

How it handles the examples:

[4,2,3] → Finds 2 (even) at index 1, which is smaller than 4
[1,2,3] → Finds 2 (even) at index 1 (1 and 3 are odd)
[] → Returns empty list immediately
[5,0,3,0,4,2] → Finds 0 at index 1, which is the smallest even value, and since we iterate left-to-right, we get the first occurrence

The algorithm naturally handles the "smallest index" requirement because we iterate from left to right and only update when we find a strictly smaller value (not equal), so the first occurrence of any minimum value is preserved.

"""

def solution3(arr):
    if not arr:
        return []
    
    smallest_even = None
    smallest_index = None
    
    for index, value in enumerate(arr):
        if value % 2 == 0:
            if smallest_even is None or value < smallest_even:
                smallest_even = value
                smallest_index = index
    
    if smallest_even is None:
        return []
    else:
        return [smallest_even, smallest_index]

#Prompting Strategy: Self Planning, LLM: Claude Sonnet 4.5
"""
Input:  
Before writing code, outline a plan that describes what functions you will implement and how they will interact. 
Then, based on your plan, write a python code for this problem
[Pasted question here]

Output: 
Plan: 
I'll create a solution with the following approach:Functions to Implement:
pluck(arr) - Main function that:

Handles the empty array edge case
Filters the array to find all even values
If no even values exist, returns []
Finds the smallest even value
Finds the first index of that smallest even value
Returns [smallest_even_value, its_index]


Algorithm Flow:
Check if the input array is empty → return []
Iterate through the array and collect all even numbers along with their indices
If no even numbers found → return []
Find the minimum even value from the collected even numbers
Return the minimum value and its index (the index is automatically the smallest since we iterate from left to right)
Key Considerations:

A number is even if num % 2 == 0
Need to track both values and their indices
Since we iterate left-to-right, the first occurrence of the minimum even value will naturally have the smallest index
Handle edge cases: empty array, no even values, multiple zeros
Now, let me implement this:
"""
def solution4(arr): 
    if not arr:
        return []
    
    even_values = []
    for i, val in enumerate(arr):
        if val % 2 == 0:
            even_values.append((val, i))
    
    if not even_values:
        return []
    
    min_even = min(even_values, key=lambda x: x[0])
    return [min_even[0], min_even[1]]


#Solution: 
def pluck(arr): 
    if(len(arr) == 0): 
        return [] 
    
    evens = list(filter(lambda x: x%2 == 0, arr)) 
    if(evens == []): 
        return [] 
    return [min(evens), arr.index(min(evens))]
        
#Test Cases: 
import numpy as np  

def check(candidate):  
    # Check some simple cases
    assert True, "This prints if this assert fails 1 (good for debugging!)" 
    assert candidate([4,2,3]) == [2, 1], "Error" 
    assert candidate([1,2,3]) == [2, 1], "Error" 
    assert candidate([]) == [], "Error" 
    assert candidate([5, 0, 3, 0, 4, 2]) == [0, 1], "Error"  

    # Check some edge cases that are easy to work out by hand. 
    assert True, "This prints if this assert fails 2 (also good for debugging!)" 
    assert candidate([1, 2, 3, 0, 5, 3]) == [0, 3], "Error" 
    assert candidate([5, 4, 8, 4 ,8]) == [4, 1], "Error" 
    assert candidate([7, 6, 7, 1]) == [6, 1], "Error" 
    assert candidate([7, 9, 7, 1]) == [], "Error"

if __name__ == "__main__":
    check(solution1)
    print("All tests passed for Solution 1!")
    check(solution2)
    print("All tests passed for Solution 2!")
    check(solution3)
    print("All tests passed for Solution 3!")
    check(solution4)
    print("All tests passed for Solution 4!")