# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        rightorder = list(reversed(postorder))
        _map = collections.defaultdict(int)
        for i, n in enumerate(inorder):
            _map[n] = i
        
        def helper(left, right):
            if left > right:
                return None
            nonlocal index
            val = rightorder[index]
            index += 1
            node = TreeNode(val)
            node.right = helper(_map[val] + 1, right)
            node.left = helper(left, _map[val] - 1)
            return node
            
        index = 0
        return helper(0, len(inorder)-1)