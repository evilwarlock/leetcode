# dp, leetcode 300, longest increasing subsequence

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        n = len(nums)

        dp = [1] * n

        for j in range(1,n):
            for i in range(j):
                if nums[j] > nums[i]:
                    dp[j] = max(dp[i]+1, dp[j]) # use dp[n] to record the longest count of increasing sequences from n-th place 
                                                # reverse order check from j, for each i < j if it is increasing

        return max(dp)


