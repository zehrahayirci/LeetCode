class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        for i in s:
            if (ord(i)<97 or ord(i)>122) and (ord(i)<48 or ord(i)>57):
                s = s.replace(i, "")
        print(s)
        return all(s[i] == s[~i] for i in range(len(s) // 2))