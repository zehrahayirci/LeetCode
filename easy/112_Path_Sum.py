# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        res = []
        self.dfs(root,targetSum,res)
        if any(res):
            return True
        return False
        
        
    def dfs(self,root,targetSum,res):
        if root:
            if not root.left and not root.right and root.val == targetSum:
                res.append(True)
            if root.left:
                self.dfs(root.left,targetSum-root.val,res)
            if root.right:
                self.dfs(root.right,targetSum-root.val,res)