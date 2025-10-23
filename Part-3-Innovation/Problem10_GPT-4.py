import random
import itertools

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

def test():
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

    for i, (ratings, expected) in enumerate(test_cases, 1):
        result = solution(ratings)
        print(f"Test {i}: Input={ratings} | Expected={expected} | Got={result} | {'PASS' if result == expected else 'FAIL'}")
    
# --- Brute-force (from actual solution given in part 1) ---
def brute_force(nums):
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


# --- Randomized test runner ---
def find_counterexample(num_tests=1000, length=6, value_range=(-10, 10)):
    for t in range(num_tests):
        n = random.randint(1, length)
        arr = [random.randint(*value_range) for _ in range(n)]
        expected = brute_force(arr)
        got = solution(arr)
        if expected != got:
            print(f"\n Counterexample found:")
            print(f"ratings = {arr}")
            print(f"Expected = {expected}, Got = {got}")
            return
    print(f"✅ No counterexamples found in {num_tests} random tests.")


if __name__ == "__main__":
    test()
    find_counterexample(num_tests=5000, length=8, value_range=(-8, 8))