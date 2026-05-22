# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

# A subarray is a contiguous non-empty sequence of elements within an array.

def subarraySum(nums, k):
        count = 0
        sum_so_far = 0
        prefix_sum_count = {0: 1}

        for num in nums:
            sum_so_far += num

            if sum_so_far - k in prefix_sum_count:
                count += prefix_sum_count[sum_so_far - k]

            prefix_sum_count[sum_so_far] = prefix_sum_count.get(sum_so_far, 0) + 1

        return count


n=int(input())
nums=list(map(int,input().split()))
k=int(input())
print(subarraySum(nums, k))
