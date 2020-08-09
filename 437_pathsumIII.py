class Solution:
    def dfs(self, root, sum, root_sum):
        if not root: return None
        
        root_sum += root.val
        self.result += self.count[root_sum]  
        self.count[root_sum + sum] += 1
        self.dfs(root.left, sum, root_sum)
        self.dfs(root.right, sum, root_sum)
        self.count[root_sum + sum] -= 1
 
    def pathSum(self, root, sum):
        self.result, self.count = 0, defaultdict(int)
        self.count[sum] = 1
        self.dfs(root, sum, 0)
        return self.result