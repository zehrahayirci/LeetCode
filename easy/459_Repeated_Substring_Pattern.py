class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        substring = ""
        lens=len(s)
        i = 1 
        while len(substring) < lens:
            substring = s[:i]
            if lens % len(substring) == 0 :
                mult = lens / len(substring)
                if mult ==1:
                    return False
                if substring * mult == s:
                    return True   
            i+=1
        return False