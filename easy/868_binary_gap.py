class Solution(object):
    def binaryGap(self, n):
        """
        :type n: int
        :rtype: int
        """
        binary = "{0:b}".format(n)
        max_gap,gap = 0,-1
        for s in binary:
            if s == '1':
                max_gap = max(max_gap,gap+1)
                gap = 0 
            elif s=='0' and gap >=0:
                gap+=1
        print(max_gap)
        return max_gap
        