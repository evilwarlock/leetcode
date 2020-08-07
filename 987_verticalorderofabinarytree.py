class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        res = []
        # dfs nodes into list with col, row, value
        def dfs(node, row, col):
            if node == None: return
            res.append( (col, row, node.val) )
            dfs(node.left, row+1, col-1)
            dfs(node.right, row+1, col+1)
        dfs(root, 0,0)
        # sort by col number
        res.sort()
        curCol = None
        output = []
        # append value of node into last element of output
        for c,r,val in res:
            if curCol != c: 
                output.append([])
                curCol = c
            output[-1].append(val)
        return output
        