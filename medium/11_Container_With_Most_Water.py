class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxh = 0 
        n = len(height)
        leftIndex = 0 
        rightIndex = n - 1
        while leftIndex < rightIndex : 
            w = rightIndex - leftIndex
            h = min(height[rightIndex],height[leftIndex])
            hacim= w * h 
            maxh = max(maxh,hacim)
            if height[leftIndex] < height[rightIndex]: 
                leftIndex +=1 
            else:
                rightIndex -=1
        return maxh