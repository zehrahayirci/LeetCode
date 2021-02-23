class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        ans = ""
        for word in d:
            a, b = len(word), len(ans)
            if a < b or (a == b and word > ans): 
                continue
            pos = -1
            for char in word:
                pos = s.find(char, pos + 1)
                if pos == -1: 
                    break
            if pos != -1: 
                ans = word
        return ans  