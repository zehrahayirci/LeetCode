class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        #all(s[i] == s[~i] for i in range(len(s) // 2))
        _hash = collections.Counter(s)
        _sum = sum(x%2 for x in _hash.values())
        return _sum <= 1