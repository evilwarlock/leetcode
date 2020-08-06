class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        if not List:
            return False
        n = len(nums) + 1
        count, res = [0] * n, []
        for i in nums:
            count[i] = count[i] + 1
            if count[i] == 2:
                res.append(i)
                
        return res
            
        
# follow up in O(n) with no extra memory?
#         