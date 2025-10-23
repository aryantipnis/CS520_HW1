import random
import math

def solution(a, b):
    if a > b:
        return 1
    if a == b:
        return 1
    
    last_digit = 1
    for num in range(a + 1, b + 1):
        last_digit = (last_digit * num) % 10
        if last_digit == 0:
            break
    return last_digit

#Solution from dataset
def calculate_expected(A, B):
    variable = 1
    if (A == B): 
        return 1
    elif ((B - A) >= 5): 
        return 0
    else: 
        for i in range(A + 1,B + 1): 
            variable = (variable * (i % 10)) % 10
        return variable % 10


def run_random_tests(num_tests=1000):
    """
    Run random tests to find counterexamples.
    """
    print(f"Running {num_tests} random tests...\n")
    
    failures = []
    
    for i in range(num_tests):
        # Generate random test cases with various ranges
        test_type = random.choice(['small', 'medium', 'large', 'edge'])
        
        if test_type == 'small':
            a = random.randint(0, 10)
            b = random.randint(0, 10)
        elif test_type == 'medium':
            a = random.randint(0, 20)
            b = random.randint(0, 20)
        elif test_type == 'large':
            a = random.randint(0, 100)
            b = random.randint(0, 100)
        else:  # edge cases
            a = random.choice([0, 1, random.randint(50, 100)])
            b = random.choice([0, 1, random.randint(50, 100)])
        
        # Get result from our solution
        result = solution(a, b)
        
        # Calculate expected (only for values where we can compute safely)
        if b <= 20:
            expected = calculate_expected(a, b)
            
            if result != expected:
                failures.append({
                    'a': a,
                    'b': b,
                    'expected': expected,
                    'got': result,
                    'test_num': i + 1
                })
                print(f"❌ FAILURE FOUND at test {i + 1}:")
                print(f"   a={a}, b={b}")
                print(f"   Expected: {expected}, Got: {result}")
                
                # Calculate what the actual product is for debugging
                if b - a <= 10:
                    product = 1
                    nums = []
                    for num in range(a + 1, b + 1):
                        product *= num
                        nums.append(num)
                    print(f"   Product: {' x '.join(map(str, nums))} = {product}")
                    print(f"   Last digit of {product} = {product % 10}\n")
                else:
                    print()
        
        # Progress indicator
        if (i + 1) % 100 == 0:
            print(f"Completed {i + 1}/{num_tests} tests...")
    
    print("\n" + "=" * 60)
    if failures:
        print(f"Found {len(failures)} FAILURES:")
        print("=" * 60)
        for f in failures:
            print(f"Test {f['test_num']}: a={f['a']}, b={f['b']} → "
                  f"Expected {f['expected']}, Got {f['got']}")
    else:
        print("All random tests PASSED! ✓")
    print("=" * 60)
    
    return failures


if __name__ == "__main__":
    # Run comprehensive random testing
    failures = run_random_tests(num_tests=2000)
    
    # If failures found, analyze them
    if failures:
        print("\n\nAnalyzing failures...")
        print("=" * 60)
        for f in failures[:5]:  # Show first 5 failures in detail
            a, b = f['a'], f['b']
            print(f"\nDetailed analysis for a={a}, b={b}:")
            print(f"Range: {a+1} to {b}")
            
            if b - a <= 10:
                nums = list(range(a + 1, b + 1))
                print(f"Numbers to multiply: {nums}")
                
                # Show step by step
                result = 1
                for num in nums:
                    old_result = result
                    result = (result * num) % 10
                    print(f"  {old_result} x {num} = {old_result * num} → last digit: {result}")