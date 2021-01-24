class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum_r=sum(nums)
        n =len(nums)
        return (n *(n+1))/2 - sum_r

        