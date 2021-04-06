class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        #[l,b,r,t]
        w = min(rec1[2],rec2[2]) - max(rec1[0],rec2[0])
        h = min(rec1[3],rec2[3]) - max(rec1[1],rec2[1])
        if w>0 and h>0:
            return True
        else: 
            return False

