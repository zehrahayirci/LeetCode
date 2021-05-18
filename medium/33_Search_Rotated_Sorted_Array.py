class Solution:
    def binarysearch(self,nums:List[int],left:int, right:int, target:int) -> int:
        while left <= right:
            middle = (left+right)//2
            if nums[middle] ==target:
                return middle
            else:
                if target < nums[middle]:
                    right = middle -1
                else:
                    left = middle +1
        return -1
    
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 1:
            return 0 if nums[0] == target else -1
        
        max_value = max(nums)
        rotate_index = nums.index(max_value)
        
        if nums[rotate_index] == target:
            return rotate_index
        
        if rotate_index ==n-1:
            return self.binarysearch(nums,0,n-1,target)
        if target < nums[0]:
            return self.binarysearch(nums,rotate_index+1,n-1,target)
        return self.binarysearch(nums,0,rotate_index,target)