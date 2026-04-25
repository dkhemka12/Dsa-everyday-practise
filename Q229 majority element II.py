# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
# The algorithm should run in linear time and in O(1) space.

def majorityElement(nums):
    freq ={}
    result =[]
    limit = len(nums)//3

    for num in nums:
        if num in freq:
            freq[num] +=1
        else:
            freq[num] =1
    for n in freq:
        if freq[n]>limit:
            result.append(n)
    return result

n = int(input())
nums = list(map(int,input().split()))
result = majorityElement(nums)
print(result)
