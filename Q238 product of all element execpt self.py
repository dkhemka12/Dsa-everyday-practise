# Given an integer array
# is equal to the product of all elements of
# nums[i] nums return an arrayanswer such thatanswer[i]equals the product of all elements ofnums
# exceptnums[i]


def productExceptSelf(nums):
    n=len(nums)
    result = [1]*n

    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= nums[i]

    suffix = 1
    for i in range(n-1,-1,-1):
        result[i]*=suffix 
        suffix *= nums[i]
    return result

n=int(input())
nums=list(map(int,input().split()))

result = productExceptSelf(nums)

print(result)