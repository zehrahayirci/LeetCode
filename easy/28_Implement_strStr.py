class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle =="" or needle==haystack:
            return 0
        elif needle not in haystack:
            return -1
        else:
            leng=len(needle)
            for i in range(0,(len(haystack)-leng)+1):
                if needle==haystack[i:i+leng]:
                    return i