# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        stack, output =[root,], []
        
        while stack:
            root=stack.pop()
            if root is not None:
                output.append(root.val)
                stack.append(root.left)            
                stack.append(root.right)
        return output[::-1]