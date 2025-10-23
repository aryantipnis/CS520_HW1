#Revised Solution 1 after debugging 
def revised_solution(ratings):
   if not ratings:
       return 0
   n = len(ratings)
   if n == 1:
       return ratings[0]


   take_prev = ratings[0] 
   skip1_prev = 0          


   for i in range(1, n):
       r = ratings[i]
       take = max(take_prev, skip1_prev) + r
       skip1 = take_prev 
       take_prev, skip1_prev = take, skip1


   ans = max(take_prev, skip1_prev)
   return ans

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
    check(revised_solution)
    print('All Test Cases Passed!')