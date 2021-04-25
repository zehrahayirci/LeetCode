# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """ 

        to_visit = []
        to_visit.append(root)
        to_visit.append(root)
        while(to_visit):
            l = to_visit.pop(0)
            r = to_visit.pop(0)
            if l == None and r == None:
                continue
            elif l == None or r == None:
                return False
            elif l.val != r.val:
                return False
            to_visit.append(l.left)
            to_visit.append(r.right)
            to_visit.append(l.right)
            to_visit.append(r.left)
        return True
