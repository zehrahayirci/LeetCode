class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        for p in s:
            if p =="(" or  p =="[" or  p =="{":
                stack.append(p)
            elif len(stack)>0:
                if p == ")":
                    if stack[-1] == "(":
                        stack.pop(-1)
                    else:
                        return False
                elif p == "]":
                    if stack[-1] == "[":
                        stack.pop(-1)
                    else:
                        return False
                elif p == "}":
                    if stack[-1] == "{":
                        stack.pop(-1)
                    else:
                        return False
            else:
                return False
        if len(stack)==0:
            return True
        else:
            return False
    
            
            