import random

def solution(a: int, b: int) -> int:
    if a >= b:
        return 1
    if (b - a) >= 5:
        return 0
    result = 1
    for i in range(a + 1, b + 1):
        result = (result * (i % 10)) % 10
    return result % 10

#Solution from dataset
def brute_force(A, B):
    variable = 1
    if (A == B): 
        return 1
    elif ((B - A) >= 5): 
        return 0
    else: 
        for i in range(A + 1,B + 1): 
            variable = (variable * (i % 10)) % 10
        return variable % 10
    

if __name__ == "__main__":
    tests = [
            ((0, 0), 1),   # factorial(0)/factorial(0) = 1
            ((5, 5), 1),   # factorial(5)/factorial(5) = 1
            ((7, 3), 1),   # a > b → special rule
            ((0, 3), 6),   # (1×2×3)=6 → last digit = 6
            ((3, 5), 0),   # (4×5)=20 → last digit = 0
            ((1, 6), 0),   # includes both 2 and 5 → last digit = 0
            ((2, 6), 0),   # (3×4×5×6)=360 → last digit = 0
            ((0, 1), 1),   # (1)=1 → last digit = 1
            ((4, 2), 1),   # a > b → 1
            ((8, 9), 9),   # (9)=9 → last digit = 9
        ]

    for (a, b), expected in tests:
        result = solution(a, b)
        print(f"solution({a}, {b}) = {result} | expected = {expected} | {'PASS' if result == expected else 'FAIL'}")

    # Random testing loop
    for _ in range(100000):
        a = random.randint(0, 50)
        b = random.randint(0, 50)
        expected = brute_force(a, b)
        result = solution(a, b)
        if result != expected:
            print(f"❌ Counterexample found: a={a}, b={b}, expected={expected}, got={result}")
            break
    else:
        print("✅ No counterexamples found in 100,000 random tests.")