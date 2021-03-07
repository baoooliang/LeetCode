# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDistance(self, root: TreeNode, p: int, q: int) -> int: 
        def dfs(node):
            if not node:
                return None
            if node.val == p or node.val == q:
                return node
            left = dfs(node.left)
            right = dfs(node.right)
            
            if left and right:
                return node
            
            return left or right
        
        res = 0
        visit = 0
        def dist(node, path):
            nonlocal res
            nonlocal visit
            if not node or visit == 2:
                return
            if node.val == p or node.val == q:
                res += path
                visit += 1
            
            dist(node.left, path+1)
            dist(node.right, path+1)
            
        
        lca = dfs(root)
        dist(lca, 0)
        return res
        
        