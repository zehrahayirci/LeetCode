class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxsum = nums[0]
        cursum =nums[0]
        for item in range(1,len(nums)):
            cursum = max(nums[item],cursum+nums[item])
            maxsum =max(maxsum,cursum)
        return maxsum
                