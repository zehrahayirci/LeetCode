class Solution(object):
    def shortestToChar(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: List[int]
        """
        answer = [-1 for i in range(len(s))]
        for i in range(len(s)):
            if s[i] == c:
                answer[i]=0
        number = 0 
        while -1 in answer:
            print(answer)
            for i in range(len(s)):
                if answer[i]== number :
                    if i > 0 and answer[i-1] == -1:
                        answer[i-1] = number+1
                    if i < len(s)-1 and answer[i+1] == -1:
                        answer[i+1] = number+1
            number +=1
        return answer