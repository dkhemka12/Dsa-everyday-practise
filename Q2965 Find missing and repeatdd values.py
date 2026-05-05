# You are given a 0-indexed 2D integer matrix grid of size n * n with values in the range [1, n2]. Each integer appears exactly once except a which appears twice and b which is missing. The task is to find the repeating and missing numbers a and b.

# Return a 0-indexed integer array ans of size 2 where ans[0] equals to a and ans[1] equals to b.

def findErrorNums(grid):
    n = len(grid)
    N = n * n
    count = [0] * (N + 1)
    
    a = b = -1

        # Count frequencies of each number
    for row in grid:
        for val in row:
                count[val] += 1
            
    # Identify the repeating (2) and missing  (0) numbers
    for i in range(1, N + 1):
        if count[i] == 2:
            a = i
        elif count[i] == 0:
            b = i
            
    return [a, b]