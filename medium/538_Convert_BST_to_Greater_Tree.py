# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
   def __init__(self):
       self.sum = 0
   def convertBST(self, root):
       """
       :type root: TreeNode
       :rtype: TreeNode
       """            
       if root is None:
           return None
       
       if root.right is None and root.left is None:
           tmp_sum = self.sum
           self.sum += root.val
           root.val += tmp_sum
           return root

       if root.right is not None:
           root.right = self.convertBST(root.right)
 
       tmp_sum = self.sum
       self.sum += root.val
       root.val += tmp_sum

       if root.left is not None:
           root.left = self.convertBST(root.left)
           
       return root
        