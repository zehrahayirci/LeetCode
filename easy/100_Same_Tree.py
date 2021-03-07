# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        current_p = p 
        current_r = q
        while (current_p):
            if not current_r:
                return False
            if current_p.val != current_r.val :
                return False 
            else:
                return ((self.isSameTree(current_p.left,current_r.left)) and (self.isSameTree(current_p.right,current_r.right)))
        if current_p == None and current_r == None:
            return True
        else:
            return False
        