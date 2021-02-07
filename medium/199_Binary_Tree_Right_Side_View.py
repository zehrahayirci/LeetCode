# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        current_level = [] 
        a = []
        if root == None:
            return []
        a.append(root.val)
        current_level.append(root)
        while len(current_level) > 0 :
            next_level = [] 
            for item in current_level:
                if item.left != None:
                    next_level.append(item.left)
                if item.right != None:
                    next_level.append(item.right)
            current_level = next_level
            if len(current_level) > 0 :
                a.append(current_level[-1].val)
        return a
