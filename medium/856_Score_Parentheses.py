class Solution(object):
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        c = 0 
        score = 0
        deep =1
        for i in range(len(S)-1):
            if S[i] == '(' and S[i+1] == ')':
                score += deep
            elif  S[i] == '(':
                deep *= 2
            elif S[i] ==')'and S[i+1] == ')':
                deep = deep / 2
        return score 