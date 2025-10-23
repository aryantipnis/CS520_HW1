"""
Problem 10 - Own Programming Problem:

Alex loves movies and maintains a list of negative and/or positive integer ratings for the movies in a collection. 
Alex is getting ready for a film festival and wants to choose some subsequence of movies from the collection to 
bring such that the following conditions are satisfied: 
• The collective sum of their ratings is maximal. 
• Alex must go through the list in order and cannot skip more than one movie in a row. 
In other words, Alex cannot skip over two or more consecutive movies. 

Example 1: 
ratings = [-1, -3, -2], Output = -3 

This must include either the second number or the first and third numbers to get a maximal rating sum of -3. 

Example 2: 
ratings = [-3, 2, 4, -1, -2, - 5], Output = 4

The maximal choices are [2, 4, -2] for a sum of 4.

Example 3: 
ratings = [9, -1, -3, 4, 5], output = 17

Alex picks the bolded items in ratings = [9, -1, -3, 4, 5] to get maximum rating = 9 + -1 + 4 + 5 = 17.

1. Happy Path Test Cases (typical valid inputs)
Test Case 1 - Mixed positives and negatives
ratings = [1, -3, 2, 4, -1, -2, -5]
# Optimal subsequence: [1, 2, 4, -2] → sum = 5

Test Case 2 - All positives
ratings = [1, 2, 3, 4, 5]
# Optimal subsequence: take all → sum = 15

Test Case 3 - Alternating positive/negative
ratings = [1, -2, 3, -1, 5]
# Optimal subsequence: [1, 3, -1, 5] → sum = 8

Test Case 4 - Skipping is necessary
ratings = [2, -10, 4, 3, -1, 5]
# Optimal subsequence: [2, 4, 3, 5] → sum = 14

Test Case 5 - Mixed small positives and negatives
ratings = [4, -1, 2, 5, -1, -3, 1]
# Optimal subsequence: [4, 2, 5, -1, 1] → sum = 11

2. Edge / Boundary Test Cases

Test Case 6 - Single movie
ratings = [10]
# Only one movie → sum = 10

Test Case 7 - Two movies
ratings = [3, 7]
# Can take both → sum = 10

Test Case 8 - All negatives
ratings = [-1, -2, -3, -4, -5]
# Must pick non-consecutive optimally → sum = -6

Test Case 9 - All zeros
ratings = [0, 0, 0, 0]
# Sum is zero regardless of subsequence → sum = 0

3. Additional Happy Path / Examples from Problem Statement
Test Case 10 - Example from problem
ratings = [-3, 2, 4, -1, -2, -5]
# Optimal subsequence: [2, 4, -2] → sum = 4

Test Case 11 - Example from problem
ratings = [9, -1, -3, 4, 5]
# Optimal subsequence: [9, -1, 4, 5] → sum = 17

Test Case 12 - Mixed positives and negatives
ratings = [-1, -3, 4, 5]
# Optimal subsequence: [4, 5] → sum = 9

"""

#Prompting Strategy: Chain of Thought, LLM: OpenAI GPT 4.0
"""
Input: 
Think step-by-step to solve this problem then write the Python code to solve this problem 
[Pasted question here]

Output: 
Step-by-step reasoning:
This problem is a variation of maximum sum subsequence with the additional constraint: cannot skip more than one movie consecutively. In other words, you cannot skip two or more movies in a row.
Step 1: Define the state
Let dp[i] be the maximum sum of a valid subsequence ending at index i, if we pick the movie at index i.
This ensures we always include i in the sum.
From i, the previous pick can be:
i-1 (previous movie picked) → allowed
i-2 (previous movie picked, skipping one) → allowed
i-3 or earlier → not allowed (because then we skipped 2 or more in a row)
So the recurrence is:
dp[i] = ratings[i] + max(
    dp[i-1] if i-1 >= 0 else 0,
    dp[i-2] if i-2 >= 0 else 0
)
Base cases:
dp[0] = ratings[0]
dp[1] = ratings[0] + ratings[1] or just ratings[1], depending on which is bigger
The final answer is max(dp), because the optimal subsequence may end at any index.

[Generated code is given below]
"""
def solution1(ratings):
    if not ratings:
        return 0
    n = len(ratings)
    if n == 1:
        return ratings[0]
    
    dp = [0] * n
    dp[0] = ratings[0]
    if n >= 2:
        dp[1] = max(ratings[0], 0) + ratings[1]  
    
    for i in range(2, n):
        dp[i] = ratings[i] + max(dp[i-1], dp[i-2])
    
    return max(dp)

#Prompting Strategy: Self Planning, LLM: GPT: 4.0
"""
Input:  
Before writing code, outline a plan that describes what functions you will implement and how they will interact. 
Then, based on your plan, write a python code for this problem
[Pasted question here]

Output: 
🧩 Step 1: Problem Understanding
We need to select a subsequence of movie ratings such that:
The sum of ratings is maximized.
We cannot skip two or more movies in a row.
We can choose to skip at most one movie between chosen movies.
The order of the list must be maintained.
This is similar to a dynamic programming problem, where we track the best sum including or excluding each movie while respecting the "cannot skip two in a row" rule.
🧠 Step 2: Define the Approach
We will use Dynamic Programming (DP):
Let dp[i] represent the maximum sum ending at index i with the rules satisfied.
Choices at position i:
Take the current movie ratings[i]:
Add it to dp[i-1] (if previous movie was taken)
Or add it to dp[i-2] (skip one movie)
Or just ratings[i] itself if starting a new sequence.
So the recurrence is:
dp[i]=ratings[i]+max(dp[i-1],dp[i-2],0)
Base cases:
dp[0] = ratings[0]
dp[1] = max(ratings[1], ratings[0] + ratings[1], ratings[0])
Finally, the answer is max(dp).
🧩 Step 3: Plan / Design
Function: max_ratings(ratings)
Steps:
Handle empty list → return 0.
Handle single-element list → return ratings[0].
Initialize dp array of same length as ratings.
Set base cases for dp[0] and dp[1].
Loop from index 2 to len(ratings)-1:
dp[i] = ratings[i] + max(dp[i-1], dp[i-2], 0)
Return max(dp).

[Generated code is given below]
"""

def solution2(ratings): 
    if not ratings:
        return 0
    n = len(ratings)
    if n == 1:
        return ratings[0]
    
    dp = [0] * n
    dp[0] = ratings[0]
    dp[1] = max(ratings[1], ratings[0] + ratings[1], ratings[0])
    
    for i in range(2, n):
        dp[i] = ratings[i] + max(dp[i-1], dp[i-2], 0)
    
    return max(dp)

#Prompting Strategy: Chain of Thought, LLM: Claude Sonnet 4.5
"""
Input: 
Think step-by-step to solve this problem then write the Python code to solve this problem 
[Pasted question here]

Output:
Step-by-Step Reasoning:
Understand the problem:

We want to find a subsequence with maximum sum
Constraint: Cannot skip more than one consecutive movie
This means: we can take adjacent movies OR skip one movie, but not skip two or more in a row



Dynamic Programming approach:

Let dp[i] = maximum sum we can get considering movies from index 0 to i
At each position i, we have two choices:

Take movie i: Then we must have taken either i-1 or i-2 (can't skip more than one)
Skip movie i: Only valid if we didn't skip i-1 (can't skip two in a row)

State definition:

We need to track whether we skipped the previous movie
dp[i][0] = max sum at position i, previous movie was taken
dp[i][1] = max sum at position i, previous movie was skipped (but i-2 was taken)


Recurrence relation:

   dp[i][0] = ratings[i] + max(dp[i-1][0], dp[i-1][1])
   // Take current movie, previous could be taken or skipped
   
   dp[i][1] = dp[i-1][0]
   // Skip current movie, previous MUST be taken
Verify with examples:

[-1, -3, -2]:

Take all: -1 + -3 + -2 = -6
Take [0,2]: -1 + -2 = -3 ✓
Take [1]: -3 ✓ (best)


[-3, 2, 4, -1, -2, -5]:

Best: [2, 4, -2] = 4 ✓
Can't take [2, 4] and skip [-1, -2] because that skips two consecutive


Python Code:

[Generate code is given below]
"""

def solution3(ratings):
    if not ratings:
        return 0
    
    n = len(ratings)
    
    if n == 1:
        return ratings[0]
    
    if n == 2:
        return max(ratings[0], ratings[1], ratings[0] + ratings[1])
    
    dp = [[float('-inf')] * 2 for _ in range(n)]
    
    dp[0][0] = ratings[0]  
    dp[0][1] = float('-inf')  
    
    dp[1][0] = max(ratings[1], ratings[0] + ratings[1])  
    dp[1][1] = ratings[0]
    
    for i in range(2, n):
        dp[i][0] = ratings[i] + max(dp[i-1][0], dp[i-1][1])
        dp[i][1] = dp[i-1][0]
    
    return max(dp[n-1][0], dp[n-1][1])

#Prompting Strategy: Self Planning, LLM: Claude Sonnet 4.5
"""
Input:  
Before writing code, outline a plan that describes what functions you will implement and how they will interact. 
Then, based on your plan, write a python code for this problem
[Pasted question here]

Output: 
PlanI'll create a solution with the following approach:Understanding the Problem:We need to find a subsequence of movies with maximum sum of ratings, with the constraint that we cannot skip more than one consecutive movie. This means:

We can take consecutive movies
We can skip one movie
We cannot skip two or more consecutive movies
This is a Dynamic Programming problem similar to "House Robber" but with different constraints.Functions to Implement:
max_rating_sum(ratings) - Main function that:

Takes a list of movie ratings (integers, can be negative or positive)
Finds the maximum sum of ratings following the constraint
Returns the maximum sum



Helper approach considerations:

Use dynamic programming to track maximum sum at each position
Track whether we took the previous movie or skipped it


Algorithm Flow:Dynamic Programming Approach:Let's define:

dp[i] = maximum rating sum we can get up to index i
At each position i, we have choices:

Take current movie: We must have taken at least one of the previous two movies
Skip current movie: Use the result from previous position


State Transition:

If we take movie at index i:

We can come from i-1 (take consecutive)
We can come from i-2 (skip one movie)
Value: ratings[i] + max(dp[i-1], dp[i-2])



If we skip movie at index i:

We must have taken movie at i-1 (can't skip two in a row)
Value: dp[i-1]


Wait, let me reconsider...Better approach:

dp[i] = maximum sum ending at position i
skip[i] = maximum sum when we skip position i
Actually, simpler approach:

At position i, we have two choices:

Take ratings[i]: add to best sum from i-1 or i-2
Skip ratings[i]: but we must have taken i-1


Let me use: dp[i][0] = max sum at i when we skip movie i
dp[i][1] = max sum at i when we take movie iRecurrence:

dp[i][1] = ratings[i] + max(dp[i-1][0], dp[i-1][1]) (take current, can come from either state)
dp[i][0] = dp[i-1][1] (skip current, must have taken previous)
Key Considerations:

Handle edge cases: empty list, single movie, two movies
Can have negative ratings, so we might be forced to take negative values
Must consider that skipping is only valid if we took the previous movie
Base cases for first two movies
Examples Verification:Example 1: [-1, -3, -2]

Options: [-1, -3], [-1, -2], or [-3]
Best: [-3] or [-1, -2] = -3 ✓
Example 2: [-3, 2, 4, -1, -2, -5]

Best path: take 2, take 4, skip -1, take -2 = 4 ✓
Example 3: [9, -1, -3, 4, 5]

Best path: take 9, skip -1, skip -3? No, can't skip two!
Actually: 9, -1, 4, 5 = 17 or 9, -3, 5 = 11, so 17 ✓
Now, let me implement this:


[Generated code is given below]
"""
def solution4(ratings): 
    if not ratings:
        return 0
    
    n = len(ratings)
    
    if n == 1:
        return ratings[0]
    
    if n == 2:
        return max(ratings[0], ratings[1], ratings[0] + ratings[1])
    
    dp = [[0, 0] for _ in range(n)]
    
    # Base cases
    dp[0][1] = ratings[0] 
    dp[0][0] = float('-inf')  
    
    dp[1][1] = ratings[1] + ratings[0] 
    dp[1][0] = ratings[0] 
    
    for i in range(2, n):
        dp[i][1] = ratings[i] + max(dp[i-1][0], dp[i-1][1])
        dp[i][0] = dp[i-1][1]
    
    return max(dp[n-1][0], dp[n-1][1])


#Solution: 
def largest_subsequence(nums):
    if not nums:
        return 0

    n = len(nums)

    if n == 1:
        return nums[0]

    dp = [0] * n
    skip = [0] * n
    dp[0] = nums[0]
    skip[0] = 0

    for i in range(1, n):
        dp[i] = max(dp[i - 1] + nums[i], skip[i - 1] + nums[i])
        skip[i] = dp[i - 1]

    return max(dp[-1], skip[-1])

        
#Test Cases: 
def check(candidate):  
    assert candidate([1, -3, 2, 4, -1, -2, -5]) == 5
    assert candidate([1, 2, 3, 4, 5]) == 15
    assert candidate([1, -2, 3, -1, 5]) == 9
    assert candidate([2, -10, 4, 3, -1, 5]) == 14
    assert candidate([4, -1, 2, 5, -1, -3, 1]) == 11
    assert candidate([10]) == 10
    assert candidate([3, 7]) == 10
    assert candidate([-1, -2, -3, -4, -5]) == -6
    assert candidate([0, 0, 0, 0]) == 0
    assert candidate([-3, 2, 4, -1, -2, -5]) == 4
    assert candidate([9, -1, -3, 4, 5]) == 17
    assert candidate([-1, -3, 4, 5]) == 8

if __name__ == "__main__":
    check(largest_subsequence)
    print("Solution Successful!")
    check(solution1)
    print("All tests passed for Solution 1!")
    check(solution2)
    print("All tests passed for Solution 2!")
    check(solution3)
    print("All tests passed for Solution 3!")
    check(solution4)
    print("All tests passed for Solution 4!")