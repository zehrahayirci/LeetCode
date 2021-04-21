class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_1 = 0
        max_2 = 0 
        for i in nums:
            if i > max_2:
                if i > max_1:
                    max_1,max_2=i,max_1
                else:
                    max_2=i
        return (max_1-1) * (max_2-1)
        