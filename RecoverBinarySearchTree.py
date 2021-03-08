# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, node):
        return self.inorder(node.left) + [node.val] + self.inorder(node.right) if node else []
    
    def findTwoNodes(self, inorder_list):
        x, y = -1, -1
        for i in range(len(inorder_list)-1):
            if inorder_list[i] > inorder_list[i+1]:
                y = inorder_list[i+1]
                if x == -1:
                    x = inorder_list[i]
                else:
                    break
        return (x,y)
    
    def recover(self, node, x, y,  counter):
        if not node:
            return
        if node.val == x or node.val == y:
            node.val = y if node.val == x else x

            counter += 1
        if counter == 2:
            return
        self.recover(node.left, x, y, counter)
        self.recover(node.right, x, y, counter)
    
    def recoverTree(self, root: TreeNode) -> None:
        inorder_list = self.inorder(root)
        x,y = self.findTwoNodes(inorder_list)

        self.recover(root, x, y, 0)
        