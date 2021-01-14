class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i, item in enumerate(nums):
            if item == target:
                return i
            if item > target:
                return i
            
        return i+1
        