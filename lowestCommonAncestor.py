
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node, p, q):
            if not node:
                return None
            if node == p or node == q:
                return node
            
            left = dfs(node.left, p, q)
            right = dfs(node.right, p, q)
            
            if not left and not right:
                return None
            if not left:
                return right
            if not right:
                return left
        return dfs(root, p, q)