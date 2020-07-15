# next permutation-31
# week 1, next permutation

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def reverse(i, j, nums):
            while i < j:
                nums[i],  nums[j] = nums[j], nums[i]
                i = i + 1
                j = j - 1

        r, curr = len(nums) - 1, len(nums) - 2
        while nums[curr] >= nums[curr + 1] and curr >= 0:
            if curr == 0:
                reverse(0, len(nums) - 1, nums) 
                return
            curr = curr -1
        reverse(curr + 1, len(nums) - 1, nums)

        l = curr + 1
        while l < r:
            mid = (l + r)//2
            if nums[mid] > nums[curr]:
                r = mid
            elif nums[mid] <= nums[curr]:
                l = mid + 1
        nums[curr], nums[r] = nums[r], nums[curr]

        return
