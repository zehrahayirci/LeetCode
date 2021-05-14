# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def height(self,root: TreeNode) -> int:
        if root is None:
            return -1
        return 1 + max(self.height(root.left),self.height(root.right))
    
    def isBalanced(self, root: TreeNode) -> bool:
        if root is None:
            return True
        if abs(self.height(root.left)-self.height(root.right)) > 1 :
            return False
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
    
    