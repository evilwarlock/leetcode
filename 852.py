# 852. Peak Index in a Mountain Array

# class Solution:
#     def peakIndexInMountainArray(self, A: List[int]) -> int:
#         # brutal force
#         for i in range(len(A)):
#             if A[i] > A[i+1]:
#                 return A[i]
        

class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        start = 0
        mid = 0
        end = len(A)

        while (start + 1 < end):
            mid = int(start + (end - start) / 2)
            if A[mid] > A[mid + 1]:
                end = mid
            elif A[mid] < A[mid + 1]:
                start = mid
        
        return start + 1





# binary search        
        
#         while (start + 1 < end):
#             mid = start + (end - start) / 2
#             if A[mid] == target:
#                 end = mid
#             elif A[mid] < target:
#                 start = mid
#             elif A[mid] > target:
#                 end = mid
                
#         if A[start] == mid:
#             return start
#         if A[end] == mid:
#             return end
                        