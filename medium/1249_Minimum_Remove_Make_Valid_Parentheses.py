class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        forth = 0 
        back = 0 
        new_s =[]
        new_r =[]
        for c in s:
            if c == '(':
                forth+=1
            if c == ')':
                if forth >0 :
                    forth-=1 
                else:
                    continue
            new_s.append(c)
        reverse_s = new_s[::-1]
        for x in reverse_s:
            if x == ')':
                back+=1
            if x == '(':
                if back >0 :
                    back-=1 
                else:
                    continue
            new_r.append(x)
        return ''.join(new_r[::-1])