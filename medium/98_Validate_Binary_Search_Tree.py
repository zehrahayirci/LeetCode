# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBinary(self,tree:TreeNode, low_range:float, high_range:float)->bool:
        if not tree:
            return True
        elif  tree.val<= low_range or  high_range <= tree.val:
            return False
        return self.isBinary(tree.left,low_range,tree.val) and self.isBinary(tree.right,tree.val,high_range)
    
    def isValidBST(self, root: TreeNode) -> bool:
        low_range = -math.inf
        high_range = math.inf
        return self.isBinary(root,low_range,high_range)