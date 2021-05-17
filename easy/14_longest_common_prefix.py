class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        answer=""
        for i in zip(*strs):
            print(i)
            if len(set(i)) == 1:
                answer += i[0]
            else:
                break
        return answer

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #Binary Search Solution:
        a = min(strs, key=len)
        l = 0
        h = len(a)
        res = ""
        while l <= h:
            m = (l + h) //2 
            print(l,h,m,a[0:m])
            flag = 1
            for item in strs:
                if not item.startswith(a[0:m]):
                    flag = 0 
            if flag:
                print("here")
                res = a[0:m]
                l = m + 1 
            else:
                print("there")
                h = m-1
                print(l,h,m)
        return res