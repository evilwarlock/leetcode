# class Solution:
#     def findDuplicates(self, nums: List[int]) -> List[int]:
#         if not List:
#             return False
#         n = len(nums) + 1
#         count, res = [0] * n, []
#         for i in nums:
#             count[i] = count[i] + 1
#             if count[i] == 2:
#                 res.append(i)
                
#         return res
            
        
# follow up in O(n) with no extra memory?
# 1. rearrange nums in order
# 2. hash nums by add "-" for visited

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        if not List:
            return False
        res = []
        for num in nums:
            if nums[abs(num)-1] > 0:
                nums[abs(num)-1] = -1 * nums[abs(num)-1]
            else:
                res.append(abs(num)) 

        return res
