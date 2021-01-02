class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s = str(x)
        rev = s[::-1]
        if rev == s:
            return True
        else:
            return False