## Problem 10 - Own Programming Problem

Alex loves movies and maintains a list of negative and/or positive integer ratings for the movies in a collection.  
Alex is getting ready for a film festival and wants to choose some subsequence of movies from the collection to bring such that the following conditions are satisfied:

- The collective sum of their ratings is **maximal**.  
- Alex must go through the list **in order** and **cannot skip more than one movie in a row**.  
  In other words, Alex cannot skip over two or more consecutive movies.

---

#### Example 1:
**Input:** `ratings = [-1, -3, -2]`  
**Output:** `-3`  
**Explanation:** This must include either the second number or the first and third numbers to get a maximal rating sum of -3.

---

#### Example 2:
**Input:** `ratings = [-3, 2, 4, -1, -2, -5]`  
**Output:** `4`  
**Explanation:** The maximal choices are `[2, 4, -2]` for a sum of 4.

---

#### Example 3:
**Input:** `ratings = [9, -1, -3, 4, 5]`  
**Output:** `17`  
**Explanation:** Alex picks the bolded items in `[9, -1, -3, 4, 5]` → sum = `9 + (-1) + 4 + 5 = 17`.

---

## 1. Happy Path Test Cases (Typical Valid Inputs)

**Test Case 1 - Mixed positives and negatives**  
`ratings = [1, -3, 2, 4, -1, -2, -5]`  
_Optimal subsequence:_ `[1, 2, 4, -2]` → **sum = 5**

---

**Test Case 2 - All positives**  
`ratings = [1, 2, 3, 4, 5]`  
_Optimal subsequence:_ take all → **sum = 15**

---

**Test Case 3 - Alternating positive/negative**  
`ratings = [1, -2, 3, -1, 5]`  
_Optimal subsequence:_ `[1, 3, -1, 5]` → **sum = 8**

---

**Test Case 4 - Skipping is necessary**  
`ratings = [2, -10, 4, 3, -1, 5]`  
_Optimal subsequence:_ `[2, 4, 3, 5]` → **sum = 14**

---

**Test Case 5 - Mixed small positives and negatives**  
`ratings = [4, -1, 2, 5, -1, -3, 1]`  
_Optimal subsequence:_ `[4, 2, 5, -1, 1]` → **sum = 11**

---

## 2. Edge / Boundary Test Cases

**Test Case 6 - Single movie**  
`ratings = [10]`  
_Only one movie →_ **sum = 10**

---

**Test Case 7 - Two movies**  
`ratings = [3, 7]`  
_Can take both →_ **sum = 10**

---

**Test Case 8 - All negatives**  
`ratings = [-1, -2, -3, -4, -5]`  
_Must pick non-consecutive optimally →_ **sum = -6**

---

**Test Case 9 - All zeros**  
`ratings = [0, 0, 0, 0]`  
_Sum is zero regardless of subsequence →_ **sum = 0**

---

## 3. Additional Happy Path / Examples from Problem Statement

**Test Case 10 - Example from problem**  
`ratings = [-3, 2, 4, -1, -2, -5]`  
_Optimal subsequence:_ `[2, 4, -2]` → **sum = 4**

---

**Test Case 11 - Example from problem**  
`ratings = [9, -1, -3, 4, 5]`  
_Optimal subsequence:_ `[9, -1, 4, 5]` → **sum = 17**

---

**Test Case 12 - Mixed positives and negatives**  
`ratings = [-1, -3, 4, 5]`  
_Optimal subsequence:_ `[4, 5]` → **sum = 9**

