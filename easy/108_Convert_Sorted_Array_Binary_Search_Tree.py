# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self,nums:List[int],left:int,right:int)-> TreeNode:
        if left > right:
            return None
        pivot = (left + right) // 2
        root = TreeNode(nums[pivot])
        root.left = self.helper(nums,left, pivot-1)
        root.right = self.helper(nums,pivot+1, right)
        return root
    
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        return self.helper(nums,0,len(nums)-1)