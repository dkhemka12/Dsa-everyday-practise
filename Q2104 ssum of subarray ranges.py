# You are given an integer array nums. The range of a subarray of nums is the difference between the largest and smallest element in the subarray.

# Return the sum of all subarray ranges of nums.

# A subarray is a contiguous non-empty sequence of elements within an array.  

def subArrayRanges(nums):
    n = len(nums)

    # Helper to calculate contribution
    def getContribution(isMin):
        stack = []
        left = [0] * n
        right = [0] * n

        # Previous less/greater
        for i in range(n):
            count = 1
            while stack and ((nums[stack[-1][0]] > nums[i]) if isMin else (nums[stack[-1][0]] < nums[i])):
                count += stack.pop()[1]
            stack.append((i, count))
            left[i] = count

        stack = []

        # Next less/greater
        for i in range(n - 1, -1, -1):
            count = 1
            while stack and ((nums[stack[-1][0]] >= nums[i]) if isMin else (nums[stack[-1][0]] <= nums[i])):
                count += stack.pop()[1]
            stack.append((i, count))
            right[i] = count

        total = 0
        for i in range(n):
            total += nums[i] * left[i] * right[i]

        return total

    sum_min = getContribution(True)
    sum_max = getContribution(False)

    return sum_max - sum_min


n=int(input())
nums=list(map(int,input().split()))

print(subArrayRanges(nums))

