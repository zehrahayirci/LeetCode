class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        index = 0
        left=0
        right =len(arr)-1
        
        return self.binarySearch(arr,left,right)
    
    def binarySearch(self,arr,left,right):
        middle = (left+right )/ 2 
        if arr[middle] > arr[middle-1] and arr[middle] > arr[middle+1]:
            return middle
        elif arr[middle] < arr[middle+1]:
            left = middle 
            return self.binarySearch(arr,left,right)
        elif arr[middle] < arr[middle-1]:
            right = middle 
            return self.binarySearch(arr,left,right)
            