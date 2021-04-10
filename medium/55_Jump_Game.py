class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dest = []
        
        if len(nums) == 1 or len(nums) == 0 :
            return True
        last_index =  len(nums)-1
        further = 0
        i =0
        while i <= further and further <= last_index:
            further = max(further,nums[i]+i)
            i+=1
        if further >= last_index:
            return True
        else:
            return False