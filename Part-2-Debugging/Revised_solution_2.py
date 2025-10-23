def revised_solution(a, b):
    difference = b - a
    if difference >= 5:
        return 0
    if difference == 0:
        return 1
    
    last_digit = 1
    for num in range(a + 1, b + 1):
        last_digit = (last_digit * num) % 10
    
    return last_digit

def check(candidate):
    # Given test cases
    assert candidate(2, 4) == 2
    assert candidate(6, 8) == 6
    assert candidate(1, 2) == 2
    assert candidate(1, 8) == 0
    assert candidate(2, 7) == 0
    assert candidate(5, 7) == 2
    assert candidate(7, 6) == 1
    assert candidate(7, 9) == 2
    assert candidate(4, 1) == 1
    assert candidate(6, 6) == 1
    assert candidate(4, 7) == 0
    assert candidate(3, 2) == 1
    assert candidate(6, 7) == 7
    assert candidate(6, 9) == 4
    assert candidate(6, 2) == 1
    assert candidate(2, 9) == 0
    assert candidate(6, 4) == 1
    assert candidate(2, 1) == 1
    assert candidate(4, 3) == 1
    assert candidate(5, 5) == 1
    assert candidate(7, 8) == 8
    assert candidate(1, 5) == 0
    assert candidate(8, 10) == 0
    assert candidate(11, 3) == 1
    assert candidate(3, 4) == 4
    assert candidate(11, 6) == 1
    assert candidate(5, 11) == 0
    assert candidate(10, 13) == 6
    assert candidate(1, 12) == 0
    assert candidate(4, 9) == 0
    assert candidate(3, 13) == 0
    assert candidate(4, 12) == 0
    assert candidate(11, 7) == 1
    assert candidate(9, 4) == 1
    assert candidate(8, 13) == 0
    assert candidate(3, 9) == 0
    assert candidate(9, 13) == 0
    assert candidate(8, 7) == 1
    assert candidate(6, 11) == 0
    assert candidate(7, 10) == 0
    assert candidate(9, 11) == 0
    assert candidate(4, 10) == 0
    assert candidate(6, 10) == 0
    assert candidate(8, 11) == 0
    assert candidate(5, 4) == 1
    assert candidate(3, 7) == 0
    assert candidate(1, 7) == 0
    assert candidate(5, 3) == 1
    assert candidate(5, 6) == 6
    assert candidate(3, 5) == 0
    assert candidate(4, 2) == 1
    assert candidate(4, 4) == 1
    assert candidate(4, 6) == 0
    assert candidate(1, 6) == 0
    assert candidate(2, 6) == 0

    # Additional provided cases
    assert candidate(3, 7) == 0
    assert candidate(20, 23) == 6
    assert candidate(1021, 1024) == 4

if __name__ == "__main__":
    check(revised_solution)
    print('All Test Cases Passed!')