# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:

# def majorityElement(nums: List[int]) -> int:
#     maxCount = 0
#     n = len(nums)

#     for i in range(n):
#         count = 0
#         for j in range(n):
#             if (nums[i] == nums[j]):
#                 count = count + 1
#         if (count > maxCount):
#             maxCount = count
#             index = i
#     if(maxCount > n/2):
#         return nums[index]        

# optimization using Moore's voting algorithm

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        major_index = 0
        count = 1
        n = len(nums)
        for i in range(n):
            if A[major_index] == A[i]:
                count = count + 1
            else:
                count = count - 1
            if count == 0:
                major_index = i
                count = 1
        return A[major_index]