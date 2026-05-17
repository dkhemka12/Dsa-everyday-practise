# Given an integer array nums, return the length of the longest strictly increasing subsequence.

def lengthOfLIS(nums):
        dp = []

        for num in nums:
            left, right = 0, len(dp)

            while left < right:
                mid = (left + right) // 2

                if dp[mid] < num:
                    left = mid + 1
                else:
                    right = mid

            if left == len(dp):
                dp.append(num)
            else:
                dp[left] = num

        return len(dp)


n=int(input())

nums=list(map(int,input().split()))
print(lengthOfLIS(nums))
