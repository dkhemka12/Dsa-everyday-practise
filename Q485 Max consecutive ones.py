# Given a binary array nums, return the maximum number of consecutive 1's in the array.

def findMaxConsecutiveOnes(nums):
    count = 0
    max_count = 0

    for num in nums:
        if num == 1:
            count += 1
        else:
            count = 0

        if count > max_count:
            max_count = count

    return max_count

n = int(input())
nums = list(map(int, input().split()))
result = findMaxConsecutiveOnes(nums)
print(result)
