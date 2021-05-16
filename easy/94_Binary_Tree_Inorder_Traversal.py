# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def printinorder(self,root:TreeNode,res:List):
        if root:
            self.printinorder(root.left,res)
            res.append(root.val)
            self.printinorder(root.right,res)
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.printinorder(root,res)
        return res
        