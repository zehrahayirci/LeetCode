class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        l = 0
        r=len(letters)-1
        return self.binarySearch(letters,target,l,r)
        
    def binarySearch(self,letters,target,l,r):
        print(r,l)
        if r-l==0:
            if target >= letters[l]:
                return letters[0]
            else:
                return letters[l]
        
        if ord(letters[int((l+r)/2)]) <= ord(target):
            return self.binarySearch(letters,target,int((l+r)/2+1),int(r))

        else:
            #print("yea i see you do you see me")
            return self.binarySearch(letters,target,l,int((r+l)/2))
        