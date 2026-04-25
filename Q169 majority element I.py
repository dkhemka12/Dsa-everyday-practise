# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

def majorityElement(nums):
    res , count =0,0
    for num in nums:
        if count==0:
            res=num
        count+=1 if num==res else -1
    return res

n = int(input())
nums = list(map(int,input().split()))
result = majorityElement(nums)
print(result)
