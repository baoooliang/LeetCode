# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def dfs(self, node, target, path):
        if not node:
            return []
        if node.val == target:
            return path + [node]
        if node.val < target:
            return self.dfs(node.right, target, path + [node])
        else:
            return self.dfs(node.left, target, path + [node])
            
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        path_p = self.dfs(root, p.val, [])
        path_q = self.dfs(root, q.val, [])

        res = root
        for i in range(min(len(path_p), len(path_q))):
            if path_p[i].val == path_q[i].val:
                res = path_p[i]
            else:
                break
        return res