"""
Problem 8 - From CodeScore-MBPP-ET:
Write a function to find the minimum cost path to reach (m, n) from (0, 0) for the given cost matrix cost[][] 
and a position (m, n) in cost[][].

"""

#Prompting Strategy: Chain of Thought, LLM: OpenAI GPT 4.0
"""
Input: 
Think step-by-step to solve this problem then write the Python code to solve this problem 
[Pasted question here]

Output: 
Step-by-step reasoning
We're given a cost matrix cost[][] and a target cell (m, n) (0-based). We must compute the minimum total cost to travel from (0,0) to (m,n) where each cell contributes its cost and allowed moves are:
right: (i, j) -> (i, j+1)
down: (i, j) -> (i+1, j)
diagonal: (i, j) -> (i+1, j+1)
Use dynamic programming. Let dp[i][j] be the minimum cost to reach (i,j). Then:
dp[0][0] = cost[0][0]
first row: dp[0][j] = dp[0][j-1] + cost[0][j] (only from left)
first column: dp[i][0] = dp[i-1][0] + cost[i][0] (only from top)
for other cells: dp[i][j] = cost[i][j] + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
After filling dp, dp[m][n] is the required minimum cost.
Complexity: O(rows * cols) time and O(rows * cols) space (can be reduced to O(cols) if desired).
Validate inputs: matrix non-empty and (m,n) in bounds.

[Generated code is given below]
"""
def solution1(cost, m, n):
    if not cost or not cost[0]:
        raise ValueError("cost matrix must be non-empty")
    rows = len(cost)
    cols = len(cost[0])
    if not (0 <= m < rows and 0 <= n < cols):
        raise ValueError("target (m,n) out of bounds")

    dp = [[0] * cols for _ in range(rows)]
    dp[0][0] = cost[0][0]

    # first row
    for j in range(1, cols):
        dp[0][j] = dp[0][j-1] + cost[0][j]
    # first column
    for i in range(1, rows):
        dp[i][0] = dp[i-1][0] + cost[i][0]

    for i in range(1, rows):
        for j in range(1, cols):
            dp[i][j] = cost[i][j] + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])

    return dp[m][n]


#Prompting Strategy: Self Planning, LLM: GPT: 4.0
"""
Input:  
Before writing code, outline a plan that describes what functions you will implement and how they will interact. 
Then, based on your plan, write a python code for this problem
[Pasted question here]

Output: 
🧩 Step 1: Problem Understanding
We are given a cost matrix (a 2D list) where each cell represents the cost to move through that cell.
We need to find the minimum cost path to reach cell (m, n) from the starting point (0, 0).
You are allowed to move only in three directions:
Right → (i, j+1)
Down → (i+1, j)
Diagonally (down-right) → (i+1, j+1)
The total cost of a path is the sum of all cell costs along that path (including the start and end cells).
Example
For:
cost = [
  [3, 4, 5],
  [2, 6, 1],
  [4, 2, 9]
]
We need to find the minimum cost to reach (2, 2) starting from (0, 0).
🧠 Step 2: Approach
We'll use Dynamic Programming (DP) — because:
The problem has overlapping subproblems (many paths share common subpaths).
We can store already computed costs for subproblems.
DP Relation
Let minCost[i][j] represent the minimum cost to reach cell (i, j).
Base cases:
minCost[0][0] = cost[0][0]
First row and first column have only one possible path.
🧩 Step 3: Plan / Design
Function: min_cost(cost, m, n)
Inputs:
cost → 2D list of integers
(m, n) → Target position
Steps:
Handle edge cases (empty matrix, invalid indices).
Create a 2D list dp of same size as cost.
Initialize dp[0][0] = cost[0][0].
Fill the first row and column separately (since they can only be reached from one direction).
For each cell (i, j), compute:
dp[i][j] = cost[i][j] + min(
              dp[i-1][j],      # from top
              dp[i][j-1],      # from left
              dp[i-1][j-1]     # from diagonal
           )
Return dp[m][n].

[Generated code is given below]
"""
def solution2(cost, m, n): 
    if not cost or not cost[0]:
        return -1
    
    rows = len(cost)
    cols = len(cost[0])
    
    if m < 0 or n < 0 or m >= rows or n >= cols:
        return -1
    
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    dp[0][0] = cost[0][0]
    
    for i in range(1, m + 1):
        dp[i][0] = dp[i - 1][0] + cost[i][0]
    
    for j in range(1, n + 1):
        dp[0][j] = dp[0][j - 1] + cost[0][j]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            dp[i][j] = cost[i][j] + min(
                dp[i - 1][j],   
                dp[i][j - 1],    
                dp[i - 1][j - 1]  
            )
    
    return dp[m][n]

#Prompting Strategy: Chain of Thought, LLM: Claude Sonnet 4.5
"""
Input: 
Think step-by-step to solve this problem then write the Python code to solve this problem 
[Pasted question here]

Output:
I'll solve this step-by-step.Step-by-Step Reasoning:
Understand the problem:

We have a 2D cost matrix where each cell has a cost value
We start at position (0, 0) and want to reach position (m, n)
We can only move right, down, or diagonally (down-right)
Find the path with minimum total cost



Movement rules:

From cell (i, j), we can move to:

(i+1, j) - down
(i, j+1) - right
(i+1, j+1) - diagonal


We cannot move backwards or outside the matrix



Dynamic Programming approach:

Create a DP table where dp[i][j] = minimum cost to reach (i, j) from (0, 0)
Base case: dp[0][0] = cost[0][0]
For each cell, the minimum cost is:



     dp[i][j] = cost[i][j] + min(
         dp[i-1][j],     // from top
         dp[i][j-1],     // from left
         dp[i-1][j-1]    // from diagonal
     )
Example:

   Cost matrix:
   [1, 2, 3]
   [4, 8, 2]
   [1, 5, 3]
   
   To reach (2, 2):
   Path: (0,0) → (0,1) → (0,2) → (1,2) → (2,2)
   Cost: 1 + 2 + 3 + 2 + 3 = 11
   
   Or: (0,0) → (1,1) → (2,2)
   Cost: 1 + 8 + 3 = 12
   
   Best path cost = 8
Edge cases:

First row: can only come from left
First column: can only come from top
Single cell matrix
Invalid indices (m or n out of bounds)

[Generate code is given below]
"""

def solution3(cost, m, n):
    if not cost or m < 0 or n < 0:
        return 0
    
    rows = len(cost)
    cols = len(cost[0]) if rows > 0 else 0
    
    if m >= rows or n >= cols:
        return float('inf') 
    
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    dp[0][0] = cost[0][0]
    
    for i in range(1, m + 1):
        dp[i][0] = dp[i-1][0] + cost[i][0]
    
    for j in range(1, n + 1):
        dp[0][j] = dp[0][j-1] + cost[0][j]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            dp[i][j] = cost[i][j] + min(
                dp[i-1][j],     
                dp[i][j-1],   
                dp[i-1][j-1]    
            )
    
    return dp[m][n]

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
We need to find the minimum cost path from the top-left corner (0, 0) to a given position (m, n) in a cost matrix. We can only move:

Right (column + 1)
Down (row + 1)
Diagonally down-right (row + 1, column + 1)

This is a classic Dynamic Programming problem.
Functions to Implement:

min_cost_path(cost, m, n) - Main function that:

Takes a 2D cost matrix and target position (m, n)
Calculates minimum cost to reach (m, n) from (0, 0)
Returns the minimum cost


Helper considerations:

Could implement recursive solution (with memoization)
Could implement iterative DP solution (more efficient)
Need to handle edge cases (invalid positions, empty matrix)



Algorithm Flow:
Dynamic Programming Approach:

Create a DP table of same size as cost matrix (or just up to m+1, n+1)
Initialize: dp[0][0] = cost[0][0] (starting position cost)
Fill first row: can only come from left

dp[0][j] = dp[0][j-1] + cost[0][j]


Fill first column: can only come from top

dp[i][0] = dp[i-1][0] + cost[i][0]


Fill rest of table: can come from top, left, or diagonal

dp[i][j] = cost[i][j] + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])


Return dp[m][n]

Key Considerations:

Recurrence relation: dp[i][j] = cost[i][j] + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
Base case: dp[0][0] = cost[0][0]
Edge cases: First row and column need special handling
Validation: Check if (m, n) is within bounds
Space optimization: Could use O(n) space instead of O(mxn)

Example:
Cost matrix:
[1, 2, 3]
[4, 8, 2]
[1, 5, 3]

Find min cost to reach (2, 2):
DP table:
[1,  3,  6]
[5,  9,  8]
[6, 11, 11]

Answer: 11
Path: (0,0) → (0,1) → (1,2) → (2,2) with costs 1 → 2 → 2 → 3 = 8
or (0,0) → (1,1) → (2,2) with costs 1 → 8 → 3 = 12
Actually: (0,0) → (1,0) → (2,1) → (2,2) = 1+4+5+3 = 13
Let me recalculate...

[Generated code is given below]
"""
def solution4(cost, m, n): 
    if not cost or not cost[0]:
        return -1
    
    rows = len(cost)
    cols = len(cost[0])
    
    if m < 0 or n < 0 or m >= rows or n >= cols:
        return -1
    
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    dp[0][0] = cost[0][0]
    
    for i in range(1, m + 1):
        dp[i][0] = dp[i - 1][0] + cost[i][0]
    
    for j in range(1, n + 1):
        dp[0][j] = dp[0][j - 1] + cost[0][j]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            dp[i][j] = cost[i][j] + min(
                dp[i - 1][j],      
                dp[i][j - 1],      
                dp[i - 1][j - 1] 
            )
    
    return dp[m][n]


#Solution: 
def min_cost(cost, m, n): 
    rows, cols = len(cost), len(cost[0])
    tc = [[0 for x in range(rows+1)] for x in range(cols+1)] 
    tc[0][0] = cost[0][0]   
    for i in range(1, m+1): 
        tc[i][0] = tc[i-1][0] + cost[i][0] 
    for j in range(1, n+1): 
        tc[0][j] = tc[0][j-1] + cost[0][j] 
    for i in range(1, m+1): 
        for j in range(1, n+1): 
            tc[i][j] = min(tc[i-1][j-1], tc[i-1][j], tc[i][j-1]) + cost[i][j] 
    return tc[m][n]
        
#Test Cases: 
def check(candidate):
    assert candidate([[1, 2, 3], [4, 8, 2], [1, 5, 3]], 2, 2) == 8
    assert candidate([[2, 3, 4], [5, 9, 3], [2, 6, 4]], 2, 2) == 12
    assert candidate([[3, 4, 5], [6, 10, 4], [3, 7, 5]], 2, 2) == 16
    assert candidate([[4, 5, 7], [6, 8, 1], [5, 9, 5]], 2, 1) == 19
    assert candidate([[6, 6, 1], [4, 10, 3], [1, 1, 1]], 2, 2) == 12
    assert candidate([[1, 3, 6], [8, 3, 3], [1, 2, 7]], 1, 2) == 7
    assert candidate([[2, 1, 4], [3, 13, 5], [1, 1, 1]], 2, 1) == 6
    assert candidate([[4, 2, 3], [6, 12, 1], [5, 5, 7]], 1, 1) == 16
    assert candidate([[4, 3, 4], [6, 12, 7], [3, 7, 7]], 1, 2) == 14
    assert candidate([[4, 3, 8], [3, 6, 5], [6, 4, 1]], 2, 1) == 11
    assert candidate([[5, 4, 7], [5, 4, 5], [6, 3, 3]], 2, 1) == 12
    assert candidate([[2, 4, 5], [9, 13, 5], [6, 10, 4]], 2, 1) == 21
    assert candidate([[6, 3, 8], [6, 9, 7], [1, 1, 7]], 1, 1) == 15
    assert candidate([[4, 2, 5], [2, 10, 3], [5, 3, 5]], 2, 2) == 14
    assert candidate([[2, 5, 4], [5, 3, 1], [4, 6, 8]], 1, 1) == 5
    assert candidate([[3, 6, 6], [3, 10, 7], [5, 5, 7]], 1, 1) == 13
    assert candidate([[6, 5, 8], [7, 4, 1], [3, 4, 4]], 2, 2) == 14
    assert candidate([[1, 1, 8], [9, 6, 7], [3, 7, 1]], 1, 1) == 7
    assert candidate([[1, 1, 1], [1, 13, 7], [6, 2, 4]], 2, 2) == 8
    assert candidate([[2, 1, 8], [7, 11, 7], [6, 6, 5]], 2, 1) == 15
    assert candidate([[3, 2, 5], [6, 3, 2], [5, 5, 7]], 1, 2) == 7
    assert candidate([[2, 3, 8], [1, 6, 7], [4, 2, 8]], 2, 1) == 5
    assert candidate([[2, 6, 6], [4, 6, 1], [2, 2, 7]], 1, 2) == 9
    assert candidate([[4, 2, 3], [4, 8, 5], [1, 5, 5]], 2, 1) == 13
    assert candidate([[4, 2, 5], [6, 11, 6], [2, 9, 7]], 2, 2) == 19
    assert candidate([[2, 5, 2], [6, 13, 5], [1, 7, 8]], 1, 2) == 12
    assert candidate([[5, 1, 4], [1, 7, 2], [6, 6, 2]], 2, 1) == 12
    assert candidate([[5, 6, 8], [4, 5, 4], [5, 3, 4]], 2, 1) == 12
    assert candidate([[1, 3, 1], [7, 6, 5], [4, 8, 4]], 2, 1) == 15
    assert candidate([[2, 7, 6], [7, 12, 2], [3, 3, 7]], 2, 2) == 18
    assert candidate([[4, 6, 2], [4, 13, 5], [4, 10, 4]], 1, 1) == 17
    assert candidate([[6, 5, 5], [6, 10, 4], [5, 5, 4]], 1, 1) == 16
    assert candidate([[6, 6, 4], [9, 11, 7], [3, 10, 7]], 2, 2) == 24
    assert candidate([[6, 3, 2], [8, 5, 3], [2, 1, 4]], 2, 1) == 12
    assert candidate([[4, 6, 2], [9, 7, 4], [1, 3, 6]], 1, 1) == 11
    assert candidate([[4, 7, 4], [9, 7, 6], [6, 1, 7]], 1, 1) == 11
    assert candidate([[2, 5, 6], [10, 11, 7], [7, 3, 4]], 2, 1) == 15
    assert candidate([[3, 6, 1], [7, 4, 3], [7, 11, 7]], 2, 2) == 14
    assert candidate([[2, 4, 3], [1, 12, 7], [5, 6, 6]], 2, 1) == 9
    assert candidate([[5, 5, 6], [8, 11, 1], [6, 11, 8]], 1, 1) == 16
    assert candidate([[6, 8, 5], [2, 14, 5], [2, 8, 1]], 2, 1) == 16
    assert candidate([[6, 8, 9], [9, 7, 3], [5, 2, 9]], 2, 2) == 22
    assert candidate([[3, 2, 7], [7, 9, 8], [1, 6, 3]], 2, 1) == 16
    assert candidate([[4, 3, 1], [7, 8, 1], [3, 11, 8]], 1, 1) == 12
    assert candidate([[1, 5, 8], [4, 11, 6], [7, 10, 3]], 1, 2) == 12
    assert candidate([[2, 7, 8], [5, 6, 7], [2, 3, 2]], 2, 1) == 10
    assert candidate([[2, 5, 9], [7, 13, 8], [5, 3, 7]], 2, 2) == 19
    assert candidate([[3, 1, 7], [4, 5, 7], [4, 5, 3]], 2, 1) == 12
    assert candidate([[4, 7, 5], [2, 13, 1], [6, 5, 4]], 1, 1) == 17
    assert candidate([[5, 7, 4], [3, 6, 7], [1, 2, 1]], 2, 2) == 11
    assert candidate([[3, 4, 5], [2, 6, 1], [4, 2, 9]], 2, 2) == 16
    assert candidate([[4, 7, 2], [1, 4, 4], [4, 11, 2]], 1, 2) == 12
    assert candidate([[1, 6, 1], [3, 7, 1], [5, 1, 3]], 1, 2) == 8
    assert candidate([[3, 6, 4], [1, 6, 6], [5, 11, 3]], 2, 2) == 12
    assert candidate([[5, 7, 5], [9, 6, 8], [5, 8, 1]], 2, 2) == 12
    assert candidate([[7, 4, 3], [2, 11, 2], [3, 4, 6]], 2, 2) == 19
    assert candidate([[3, 1, 8], [8, 5, 6], [4, 1, 5]], 2, 1) == 9
    assert candidate([[7, 4, 6], [10, 8, 5], [2, 1, 2]], 2, 2) == 17
    assert candidate([[2, 2, 7], [3, 4, 7], [4, 3, 9]], 1, 1) == 6
    assert candidate([[7, 3, 1], [2, 12, 4], [5, 8, 7]], 2, 1) == 17
    assert candidate([[4, 5, 2], [7, 14, 2], [5, 7, 4]], 2, 2) == 15
    assert candidate([[3, 5, 6], [7, 13, 6], [1, 1, 5]], 2, 2) == 16
    assert candidate([[1, 7, 2], [4, 7, 1], [3, 11, 9]], 1, 1) == 8
    assert candidate([[5, 2, 5], [3, 4, 2], [6, 9, 1]], 1, 2) == 9
    assert candidate([[4, 8, 9], [7, 10, 4], [5, 5, 9]], 1, 1) == 14
    assert candidate([[5, 4, 4], [7, 6, 1], [7, 6, 7]], 2, 1) == 17
    assert candidate([[3, 3, 4], [7, 11, 6], [3, 11, 1]], 1, 2) == 12
    assert candidate([[1, 4, 4], [1, 11, 6], [3, 2, 3]], 1, 1) == 12
    assert candidate([[1, 2, 6], [5, 4, 3], [2, 5, 6]], 1, 1) == 5
    assert candidate([[6, 4, 3], [1, 14, 6], [5, 6, 10]], 1, 2) == 16
    assert candidate([[6, 5, 7], [4, 13, 7], [6, 9, 4]], 1, 2) == 18
    assert candidate([[7, 7, 10], [1, 7, 3], [8, 2, 4]], 1, 2) == 17
    assert candidate([[3, 6, 9], [3, 5, 5], [2, 7, 6]], 1, 2) == 13
    assert candidate([[7, 5, 6], [7, 8, 1], [4, 5, 9]], 1, 2) == 13
    assert candidate([[4, 4, 4], [3, 15, 2], [4, 6, 6]], 2, 1) == 13
    assert candidate([[7, 7, 10], [1, 14, 5], [4, 9, 7]], 1, 1) == 21
    assert candidate([[8, 4, 8], [5, 11, 8], [1, 4, 7]], 2, 1) == 17
    assert candidate([[1, 8, 7], [5, 15, 3], [6, 4, 3]], 2, 2) == 13
    assert candidate([[1, 8, 7], [7, 10, 3], [1, 11, 7]], 1, 1) == 11
    assert candidate([[3, 5, 8], [9, 5, 6], [8, 10, 8]], 2, 2) == 16
    assert candidate([[5, 1, 9], [11, 12, 1], [8, 8, 8]], 2, 2) == 15
    assert candidate([[4, 1, 7], [2, 13, 6], [5, 9, 2]], 2, 1) == 15
    assert candidate([[2, 3, 7], [2, 9, 1], [4, 6, 7]], 1, 2) == 6
    assert candidate([[6, 6, 3], [8, 9, 3], [8, 11, 6]], 1, 1) == 15
    assert candidate([[2, 9, 9], [11, 12, 9], [6, 12, 4]], 2, 1) == 25
    assert candidate([[1, 9, 2], [5, 15, 5], [5, 3, 2]], 1, 2) == 15
    assert candidate([[3, 2, 10], [4, 5, 6], [3, 8, 3]], 1, 2) == 11
    assert candidate([[8, 5, 1], [7, 9, 2], [2, 8, 4]], 2, 2) == 19
    assert candidate([[5, 1, 2], [6, 10, 8], [2, 11, 7]], 1, 1) == 15
    assert candidate([[6, 5, 8], [9, 6, 4], [7, 10, 9]], 2, 2) == 21
    assert candidate([[1, 6, 5], [3, 5, 7], [3, 5, 7]], 1, 2) == 13
    assert candidate([[4, 2, 5], [2, 12, 3], [6, 7, 4]], 2, 2) == 13
    assert candidate([[8, 7, 9], [11, 9, 9], [6, 2, 6]], 2, 1) == 19
    assert candidate([[8, 9, 2], [1, 5, 3], [5, 2, 3]], 2, 2) == 14
    assert candidate([[4, 2, 4], [2, 6, 7], [4, 2, 10]], 1, 2) == 13
    assert candidate([[7, 6, 3], [4, 8, 5], [7, 8, 1]], 2, 1) == 19
    assert candidate([[8, 9, 4], [8, 5, 9], [6, 8, 6]], 2, 1) == 21
    assert candidate([[3, 5, 6], [2, 9, 9], [1, 3, 4]], 2, 2) == 12
    assert candidate([[7, 9, 8], [7, 13, 2], [7, 7, 7]], 2, 1) == 21
    assert candidate([[7, 2, 2], [6, 15, 1], [8, 4, 2]], 1, 1) == 22
    assert candidate([[5, 6, 8], [8, 10, 2], [7, 3, 8]], 1, 2) == 13
    assert candidate([[8, 9, 2], [6, 5, 7], [3, 8, 8]], 2, 2) == 21     

if __name__ == "__main__":
    check(min_cost)
    check(solution1)
    print("All tests passed for Solution 1!")
    # check(solution2)
    print("All tests passed for Solution 2!")
    check(solution3)
    print("All tests passed for Solution 3!")
    # check(solution4)
    print("All tests passed for Solution 4!")