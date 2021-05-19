class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag = collections.Counter(magazine)           
        ran = collections.Counter(ransomNote)
        
        print(set(mag))
        print(set(ran))
        
        if len(ransomNote) > len(magazine): return False
        
        for r in ransomNote:
            if mag[r] <= 0:
                return False
            mag[r] -=1
        return True
        