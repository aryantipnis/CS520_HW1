
import random

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


def brute_force_solution(nums):
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


def test_random_cases(num_tests=1000, max_length=10):
    """
    Test the solution against brute force on random inputs.
    """
    print(f"Running {num_tests} random tests...")
    failures = []
    
    for test_num in range(num_tests):
        # Generate random test case
        length = random.randint(1, max_length)
        ratings = [random.randint(-20, 20) for _ in range(length)]
        
        # Get results from both solutions
        our_result = solution(ratings)
        correct_result = brute_force_solution(ratings)
        
        # Check if they match
        if our_result != correct_result:
            failures.append({
                'test_num': test_num + 1,
                'input': ratings,
                'our_result': our_result,
                'correct_result': correct_result
            })
            print(f"\n❌ FAILURE FOUND - Test #{test_num + 1}")
            print(f"Input:    {ratings}")
            print(f"Our result: {our_result}")
            print(f"Expected:   {correct_result}")
            
            # Stop after finding first failure for analysis
            return failures
    
    print(f"\n✓ All {num_tests} tests passed!")
    return failures


def analyze_failure(ratings):
    """
    Detailed analysis of a failing test case.
    """
    print("\n=== DETAILED ANALYSIS ===")
    print(f"Input: {ratings}")
    
    n = len(ratings)
    take = [0] * n
    skip = [float('-inf')] * n
    
    take[0] = ratings[0]
    skip[0] = 0
    
    print(f"\nStep 0:")
    print(f"  take[0] = {take[0]} (taking movie {ratings[0]})")
    print(f"  skip[0] = {skip[0]} (skipping first, sum = 0)")
    
    for i in range(1, n):
        take[i] = ratings[i] + max(take[i - 1], skip[i - 1])
        skip[i] = take[i - 1]
        
        print(f"\nStep {i}:")
        print(f"  ratings[{i}] = {ratings[i]}")
        print(f"  take[{i}] = {ratings[i]} + max({take[i-1]}, {skip[i-1]}) = {take[i]}")
        print(f"  skip[{i}] = take[{i-1}] = {skip[i]}")
    
    print(f"\nFinal: max(take[-1], skip[-1]) = max({take[-1]}, {skip[-1]}) = {max(take[-1], skip[-1])}")
    
    # Show brute force result
    correct = brute_force_solution(ratings)
    print(f"\nBrute force result: {correct}")


if __name__ == "__main__":
    # First run the original test cases
    print("=== Running Original Test Cases ===")
    test_cases = [
        ([5], 5),
        ([-10], -10),
        ([3, 7], 10),
        ([10, -5], 10),
        ([-5, -2, -8, -1], -3),
        ([-1, -3, -2], -3),
        ([-3, 2, 4, -1, -2, -5], 4),
        ([9, -1, -3, 4, 5], 17),
        ([1, -10, -10, 100], 81),
        ([20, -15, 18, -12, 25], 46),
    ]
    
    all_passed = True
    for i, (input_data, expected) in enumerate(test_cases, 1):
        result = solution(input_data)
        if result == expected:
            print(f"Test {i}: ✓ PASS")
        else:
            print(f"Test {i}: ✗ FAIL - Input: {input_data}, Expected: {expected}, Got: {result}")
            all_passed = False
    
    if all_passed:
        print("\n✓ All original tests passed!")
    
    # Now run random tests
    print("\n" + "="*50)
    print("=== Running Random Tests ===")
    failures = test_random_cases(num_tests=1000, max_length=10)
    
    if failures:
        print(f"\n\nFound {len(failures)} failure(s)")
        for failure in failures:
            analyze_failure(failure['input'])
    else:
        print("\n🎉 No failures found in random testing!")