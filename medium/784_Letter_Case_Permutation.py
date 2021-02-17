from itertools import product
class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        a =  list(map(''.join, product(*zip(S.lower(), S.upper()))))
        return set(a)