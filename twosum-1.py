# twosum-1

class Solution:
    # def twoSum(self, nums, target):
    #     if not nums:
    #         return 0
    #     # print(target)
    #     n = len(nums)
    #     # print(n)
    #     for i in range(n):
    #         for j in range(i+1, n):
    #             print(i,j)
    #             if nums[i] + nums[j] == target:
    #                 return [i, j]
            
    def twoSum(self, nums, target):
        if not nums:
            return 0

        n = len(nums)
        # nums.sort()

        # lo, hi = 0, n-1

        # while lo < hi:
        #     if nums[lo] + nums[hi] == target:
        #         return [lo+1, hi]
        #     elif nums[lo] + nums[hi] < target:
        #         lo = lo + 1
        #     else:
        #         hi = hi - 1

        d = {}
        for i in range(n):
            z = target - nums[i]

            if z in d:
                return [d[z], i]
            else:
                d[nums[i]] = i


test = Solution()
print(test.twoSum([3,2,4],6))