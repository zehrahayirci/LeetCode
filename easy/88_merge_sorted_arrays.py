class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        #This is faster 
        k = m+n-1
        i = m-1
        j = n-1
        while k>-1 :
            if i == - 1:
                nums1[k] = nums2[j]
                j-=1
            elif j==-1:
                nums1[k] = nums1[i]
                i-=1            
            elif nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i-=1
            else:
                nums1[k] = nums2[j]
                j-=1
            k-=1
        #this is brute force
    def merge2(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(n):
            nums1[i + m] = nums2[i]
        nums1.sort()