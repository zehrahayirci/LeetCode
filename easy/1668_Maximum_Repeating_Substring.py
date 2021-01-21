class Solution(object):
    def maxRepeating(self, sequence, word):
        """
        :type sequence: str
        :type word: str
        :rtype: int
        """
        count=0
        for i in range(len(sequence)+1):
            if word*i in sequence:
                count=i
        return count
        