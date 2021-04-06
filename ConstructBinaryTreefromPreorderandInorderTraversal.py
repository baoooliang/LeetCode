# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        _map = collections.defaultdict(int)
        for i, n in enumerate(inorder):
            _map[n] = i
        
        def build_sub_tree(left, right):
            nonlocal index
            
            if left > right:
                return None
            
            root  = TreeNode(preorder[index])
            i_inorder = _map[preorder[index]]
            index += 1
            root.left = build_sub_tree(left, i_inorder-1)
            root.right = build_sub_tree(i_inorder+1, right)
            return root
        
        index = 0
        return build_sub_tree(0, len(inorder)-1)