# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBranch(self, node:TreeNode) -> bool:
        if node.left or node.right:
            return False
        return True
    
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        elif (not root.left ) and (not root.right):
            return [root.val]
        
        #Left
        left_res = [root.val]
        t = root.left
        while t:
            if not self.isBranch(t):
                left_res.append(t.val)
            if t.left:
                t = t.left
            else:
                t = t.right
        
        #print(left_res)
        
           
        #Right 
        right_res =  []
        r = root.right
        while(r):
            if not self.isBranch(r):
                right_res.append(r.val)
            if r.right:
                r=r.right
            else:
                r= r.left
                
        #print(right_res)
        
        #Bottom
        bottom_res = []
        bottom_stack=[root]
        while(bottom_stack):
            node = bottom_stack.pop()
            if node:
                if node.left == None and node.right == None:
                    bottom_res.append(node.val)
                bottom_stack.append(node.right)
                bottom_stack.append(node.left)
        #print(bottom_res)
        
        return left_res + bottom_res + right_res[::-1]