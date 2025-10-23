## Problem 10 using GPT-4 model

Let's apply the new proposed strategy to this problem 

### Step 1: Planner: 

```
You are a planner. Problem: [Paste problem statement here].
1) Briefly (3–6 bullet points) outline the approach and the key constraint to maintain.*
2) List the 6 most important edge cases we must test.
```

***Generated Code:***
```
1️⃣ Approach Outline
Dynamic Programming setup:

Maintain two DP states for each index i:
take[i]: Maximum sum if you take the i-th movie.
skip[i]: Maximum sum if you skip the i-th movie.

Key constraint to maintain:
You cannot skip more than one movie in a row — i.e., if you skipped movie i-1, you must take movie i

Transition logic:
If you take i:
take[i] = ratings[i] + max(take[i-1], skip[i-1])
If you skip i:
You can only skip if the previous movie was taken → skip[i] = take[i-1]

Base cases:
take[0] = ratings[0]
skip[0] = -inf (you can’t skip the very first movie, otherwise you might skip two right away)

Final answer:
max(take[n-1], skip[n-1]) gives the maximal achievable sum under the skip constraint.

2️⃣ Six Most Important Edge Cases

All negative ratings → e.g. [-5, -2, -7]
→ Should return the least negative valid combination (like -2 or sum of allowed negatives).

All positive ratings → e.g. [1, 2, 3, 4]
→ Should take all movies (no reason to skip) → output = sum of all.

Single element → e.g. [7]
→ Must take it → output = 7.

Two elements → e.g. [4, -5]
→ Can take either one or both → test simple transitions.

Constraint pressure (forcing skips) → e.g. [10, -9, -8, 10]
→ Ensures skipping only one in a row is properly enforced.

Mixed positive and negative near edges → e.g. [-3, 5, -1, -2, 6]
→ Tests dynamic selection balancing skip constraint and cumulative sum.
```

### Step 2: Tester:
```
You are a Tester. Using the plan and edge cases from Planner, produce 10 unit tests in Python: a list of (input, expected_output). Include comments saying why each test matters.
```

***Generated Code:***

```python 
test_cases = [
    # 1️⃣ Single positive element
    # Must take it — simplest non-empty input.
    ([7], 7),

    # 2️⃣ Single negative element
    # Must take it (no skip possible), output = that negative number.
    ([-5], -5),

    # 3️⃣ Two elements, both positive
    # Take both → 3 + 5 = 8
    ([3, 5], 8),

    # 4️⃣ Two elements, one negative
    # Either take first or both, depending on total → max(4, 4 + -5 = -1) = 4
    ([4, -5], 4),

    # 5️⃣ All negatives
    # Example from edge case: choose least harmful valid combination.
    # [-5, -2, -7] → take second (-2) gives max sum.
    ([-5, -2, -7], -2),

    # 6️⃣ All positives
    # Should take all → sum([1, 2, 3, 4]) = 10
    ([1, 2, 3, 4], 10),

    # 7️⃣ Mixed signs forcing optimal skipping
    # Example from prompt: [-3, 2, 4, -1, -2, -5] → max sum = 4
    ([-3, 2, 4, -1, -2, -5], 4),

    # 8️⃣ Large positive then deep negatives then positive
    # [10, -9, -8, 10] → best: take first (10), skip one (-9), must take (-8), skip? no, take last = 10 + (-8) + 10 = 12
    ([10, -9, -8, 10], 12),

    # 9️⃣ Alternating negatives and positives
    # [-3, 5, -1, -2, 6] → best combo [5, -1, 6] = 10
    ([-3, 5, -1, -2, 6], 10),

    # 🔟 Example from prompt with strong positives at start and end
    # [9, -1, -3, 4, 5] → pick 9, -1, 4, 5 = 17
    ([9, -1, -3, 4, 5], 17),
]
```

### Step 3: Coder:
```
You are a Coder. Implement the function `solution(args...)` described below. Use the plan and tests from Planner/Tester. Write clean, well-commented Python code and include the tests as a `if __name__ == "__main__":` block to run them.
Problem: [Paste problem statement here with test cases]
Return only the code file.
```

***Generated Code:***
```python 
def solution(ratings):
    n = len(ratings)
    if n == 0:
        return 0

    take = [0] * n
    skip = [float('-inf')] * n
    take[0] = ratings[0]

    for i in range(1, n):
        take[i] = ratings[i] + max(take[i - 1], skip[i - 1])
        skip[i] = take[i - 1]

    return max(take[-1], skip[-1])


if __name__ == "__main__":
    test_cases = [
        # 1. Mixed positives and negatives
        ([1, -3, 2, 4, -1, -2, -5], 5),
        # 2. All positives
        ([1, 2, 3, 4, 5], 15),
        # 3. Alternating positive/negative
        ([1, -2, 3, -1, 5], 9),
        # 4. Skipping necessary
        ([2, -10, 4, 3, -1, 5], 14),
        # 5. Mixed small positives and negatives
        ([4, -1, 2, 5, -1, -3, 1], 11),
        # 6. Single movie
        ([10], 10),
        # 7. Two movies
        ([3, 7], 10),
        # 8. All negatives
        ([-1, -2, -3, -4, -5], -6),
        # 9. All zeros
        ([0, 0, 0, 0], 0),
        # 10. Example from problem (-3, 2, 4, -1, -2, -5)
        ([-3, 2, 4, -1, -2, -5], 4),
        # 11. Example from problem (9, -1, -3, 4, 5)
        ([9, -1, -3, 4, 5], 17),
        # 12. Mixed positives and negatives (-1, -3, 4, 5)
        ([-1, -3, 4, 5], 8),
    ]

    # Run and print results
    for i, (ratings, expected) in enumerate(test_cases, 1):
        result = solution(ratings)
        print(f"Test {i}: Input={ratings} | Expected={expected} | Got={result} | {'PASS' if result == expected else 'FAIL'}")
```
### Step 4: Run Tests

After running the above code locally, I found that the above code failed for these 2 test cases when input = [-1, -2, -3, -4, -5] and input = [-3, 2, 4, -1, -2, -5].

### Step 5: Refinement

```
The following tests failed when input = [-1, -2, -3, -4, -5] expected was -6 we got -7 and input = [-3, 2, 4, -1, -2, -5] expected was 4 we got 1. Generate a code that takes into account this failing test case. Take into account that you cannot skip more than one element and for all negative values the result should be maximum
```

***Generated Code***: 

```python
def solution(ratings):

    n = len(ratings)
    if n == 0:
        return 0

    if n == 1:
        return ratings[0]

    take = [0] * n
    skip = [float('-inf')] * n

    take[0] = ratings[0]
    skip[0] = 0 

    for i in range(1, n):
        take[i] = ratings[i] + max(take[i - 1], skip[i - 1])
        skip[i] = take[i - 1]

    return max(take[-1], skip[-1])
```

This passes all the failed test cases in previous steps.

### Step 6: Counterexample Search:

```
Run this code over random inputs to find a counterexample that fails the test.
```

***Generated Code***: 

```python
# --- Randomized test runner ---
def find_counterexample(num_tests=1000, length=6, value_range=(-10, 10)):
    for t in range(num_tests):
        n = random.randint(1, length)
        arr = [random.randint(*value_range) for _ in range(n)]
        expected = brute_force(arr)
        got = solution(arr)
        if expected != got:
            print(f"\n❌ Counterexample found:")
            print(f"ratings = {arr}")
            print(f"Expected = {expected}, Got = {got}")
            return
    print(f"✅ No counterexamples found in {num_tests} random tests.")


if __name__ == "__main__":
    find_counterexample(num_tests=5000, length=8, value_range=(-8, 8))
```

There were no counter examples, thus we can assume that the code we have is correct. 