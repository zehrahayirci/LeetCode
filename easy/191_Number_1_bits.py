
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        s=0
        string="{0:b}".format(n)
        print(string)
        for i in string:
            if i == '1':
                s+=1
        return s
        