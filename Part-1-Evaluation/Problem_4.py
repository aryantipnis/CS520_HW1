"""
Problem 4 - From HumanEval/74: 

Write a function that accepts two lists of strings and returns the list that has total number of chars in the all strings of the list less than the other list.  
If the two lists have the same number of chars, return the first list.  

Examples: 
total_match([], []) ➞ [] 
total_match(['hi', 'admin'], ['hI', 'Hi']) ➞ ['hI', 'Hi'] 
total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']) ➞ ['hi', 'admin'] 
total_match(['hi', 'admin'], ['hI', 'hi', 'hi']) ➞ ['hI', 'hi', 'hi'] 
total_match(['4'], ['1', '2', '3', '4', '5']) ➞ ['4']
"""

#Prompting Strategy: Chain of Thought, LLM: OpenAI GPT 4.0
"""
Input: 
Think step-by-step to solve this problem then write the Python code to solve this problem 
[Pasted question here]

Output: 
Step-by-step reasoning
For each list, compute the total number of characters by summing the lengths of every string in that list.
Compare the two totals:
If sum(list1) ≤ sum(list2), return list1 (the problem specifies returning the first list on ties).
Otherwise return list2.
Handle empty lists naturally (sum of lengths will be 0).

[Generated code is given below]
"""
def solution1(list1, list2): 
    sum1 = sum(len(s) for s in list1)
    sum2 = sum(len(s) for s in list2)
    return list1 if sum1 <= sum2 else list2


#Prompting Strategy: Self Planning, LLM: GPT: 4.0
"""
Input:  
Before writing code, outline a plan that describes what functions you will implement and how they will interact. 
Then, based on your plan, write a python code for this problem
[Pasted question here]

Output: 
🧠 Step 1: Problem Understanding
We are given two lists of strings, and we need to:
Compute the total number of characters across all strings in each list.
Return the list with the smaller total number of characters.
If both totals are equal, return the first list.
🧩 Example Walkthroughs
List 1	List 2	Total Chars (L1)	Total Chars (L2)	Output
[]	[]	0	0	[]
['hi', 'admin']	['hI', 'Hi']	7	4	['hI', 'Hi']
['hi', 'admin']	['hi', 'hi', 'admin', 'project']	7	16	['hi', 'admin']
['hi', 'admin']	['hI', 'hi', 'hi']	7	6	['hI', 'hi', 'hi']
['4']	['1', '2', '3', '4', '5']	1	5	['4']

🧩 Step 2: Plan / Design
Function 1: total_match(list1, list2)
Purpose:
Compare total character counts of two lists of strings and return the list with fewer total characters.
Steps:
Compute total characters for list1:
Use a comprehension: sum(len(s) for s in list1)
Compute total characters for list2:
Use a comprehension: sum(len(s) for s in list2)
Compare totals:
If total1 < total2 → return list1
If total2 < total1 → return list2
If totals are equal → return list1 (as per problem statement)

⚙️ Step 3: Function Interaction
There is only one function, total_match().
It's completely self-contained — it takes two lists and returns one list.
No helper functions are needed because the logic is simple.

[Generated code is given below]
"""

def solution2(list1, list2): 
    total1 = sum(len(s) for s in list1)
    total2 = sum(len(s) for s in list2)
    
    if total1 <= total2:
        return list1
    else:
        return list2

#Prompting Strategy: Chain of Thought, LLM: Claude Sonnet 4.5
"""
Input: 
Think step-by-step to solve this problem then write the Python code to solve this problem 
[Pasted question here]

Output:
Step-by-Step Reasoning:

Understand the problem:

Compare two lists of strings
Calculate the total number of characters in all strings for each list
Return the list with fewer total characters
If both lists have the same total, return the first list


Verify with examples:

[], []:

List 1 total: 0 chars
List 2 total: 0 chars
Same → return first list: [] ✓

['hi', 'admin'], ['hI', 'Hi']:

List 1: 'hi'(2) + 'admin'(5) = 7 chars
List 2: 'hI'(2) + 'Hi'(2) = 4 chars
4 < 7 → return list 2: ['hI', 'Hi'] ✓


['hi', 'admin'], ['hi', 'hi', 'admin', 'project']:

List 1: 2 + 5 = 7 chars
List 2: 2 + 2 + 5 + 7 = 16 chars
7 < 16 → return list 1: ['hi', 'admin'] ✓


['hi', 'admin'], ['hI', 'hi', 'hi']:

List 1: 2 + 5 = 7 chars
List 2: 2 + 2 + 2 = 6 chars
6 < 7 → return list 2: ['hI', 'hi', 'hi'] ✓

['4'], ['1', '2', '3', '4', '5']:

List 1: 1 char
List 2: 1 + 1 + 1 + 1 + 1 = 5 chars
1 < 5 → return list 1: ['4'] ✓

Algorithm:

Calculate total characters in list 1
Calculate total characters in list 2
Compare and return the list with fewer characters
If equal, return list 1


Implementation approach:

Use sum() with len() to calculate total characters
Use conditional logic to return the appropriate list


[Generate code is given below]
"""

def solution3(lst1, lst2): 
    total1 = sum(len(s) for s in lst1)
    total2 = sum(len(s) for s in lst2)

    if total1 <= total2:
        return lst1
    else:
        return lst2

#Prompting Strategy: Self Planning, LLM: Claude Sonnet 4.5
"""
Input:  
Before writing code, outline a plan that describes what functions you will implement and how they will interact. 
Then, based on your plan, write a python code for this problem
[Pasted question here]

Output: 
Plan
I'll create a solution with the following approach:
Functions to Implement:

total_match(lst1, lst2) - Main function that:

Takes two lists of strings as input
Calculates the total number of characters in all strings of list1
Calculates the total number of characters in all strings of list2
Compares the totals and returns the list with fewer total characters
If totals are equal, returns the first list


Algorithm Flow:

Calculate total characters in lst1:

Iterate through all strings in lst1
Sum the length of each string

Calculate total characters in lst2:

Iterate through all strings in lst2
Sum the length of each string

Compare the totals:

If total1 <= total2, return lst1 (handles equal case)
Otherwise, return lst2


Key Considerations:

Use sum(len(s) for s in lst) to calculate total characters efficiently
Handle empty lists (total chars = 0)
Use <= comparison to ensure first list is returned when totals are equal
Character count is case-sensitive (each character counts as 1)

Verification with Examples:

[], [] → both have 0 chars → return first list = [] ✓
['hi', 'admin'], ['hI', 'Hi'] → (2+5=7) vs (2+2=4) → return second = ['hI', 'Hi'] ✓
['hi', 'admin'], ['hi', 'hi', 'admin', 'project'] → (2+5=7) vs (2+2+5+7=16) → return first = ['hi', 'admin'] ✓
['hi', 'admin'], ['hI', 'hi', 'hi'] → (2+5=7) vs (2+2+2=6) → return second = ['hI', 'hi', 'hi'] ✓
['4'], ['1', '2', '3', '4', '5'] → (1) vs (1+1+1+1+1=5) → return first = ['4'] ✓

Now, let me implement this:

[Generated code is given below]
"""
def solution4(lst1, lst2): 
    total1 = sum(len(s) for s in lst1)
    total2 = sum(len(s) for s in lst2)
    
    if total1 <= total2:
        return lst1
    else:
        return lst2

#Solution: 
def total_match(lst1, lst2): 
    l1 = 0 
    for st in lst1: 
        l1 += len(st)  
    
    l2 = 0 
    for st in lst2: 
        l2 += len(st)  

    if l1 <= l2: 
        return lst1 
    else: 
        return lst2
        
#Test Cases: 
def check(candidate):  
    # Check some simple cases 
    assert True, "This prints if this assert fails 1 (good for debugging!)" 
    assert candidate([], []) == [] 
    assert candidate(['hi', 'admin'], ['hi', 'hi']) == ['hi', 'hi'] 
    assert candidate(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']) == ['hi', 'admin'] 
    assert candidate(['4'], ['1', '2', '3', '4', '5']) == ['4'] 
    assert candidate(['hi', 'admin'], ['hI', 'Hi']) == ['hI', 'Hi'] 
    assert candidate(['hi', 'admin'], ['hI', 'hi', 'hi']) == ['hI', 'hi', 'hi'] 
    assert candidate(['hi', 'admin'], ['hI', 'hi', 'hii']) == ['hi', 'admin']   
    
    # Check some edge cases that are easy to work out by hand. 
    assert True, "This prints if this assert fails 2 (also good for debugging!)" 
    assert candidate([], ['this']) == [] 
    assert candidate(['this'], []) == [] 

if __name__ == "__main__":
    check(solution1)
    print("All tests passed for Solution 1!")
    check(solution2)
    print("All tests passed for Solution 2!")
    check(solution3)
    print("All tests passed for Solution 3!")
    check(solution4)
    print("All tests passed for Solution 4!")