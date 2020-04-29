# 1351. Count Negative Numbers in a Sorted Matrix
# class Solution(object):
#     def countNegatives(self, grid):
#         """
#         :type grid: List[List[int]]
#         :rtype: int
#         """
#         # if grid == []:
#         #     return 
#         # 4  3   2   1
#         # 3  2   1  -1
#         # 1  1  -1  -2
#         # -1 -1 -2  -3
#         count = 0
#         m = len(grid)
#         n = len(grid[0])
#         for i in range(m):
#             for j in range(n):
#                 if grid[i][j] < 0:
#                     count = count + 1
        
#         return count
    
        # o(m*n)
        
        # follow up O(m+n)
# optimized find the left most negative number skip the rest in each row        
class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # if grid == []:
        #     return 
        # 4  3   2   1
        # 3  2   1  -1
        # 1  1  -1  -2
        # -1 -1 -2  -3
        count = 0
        # m = len(grid)
        # n = len(grid[0])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] < 0:
                    count = count + len(grid[i]) - j
                    break
        
        return count