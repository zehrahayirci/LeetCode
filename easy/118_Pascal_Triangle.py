class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        i = 1
        pascal = []
        while i <= numRows:
            if i ==1:
                pascal.append([1])
            elif i == 2:
                pascal.append([1,1])
            else:
                last = pascal[i-2]
                arr = [1] * i 
                arr[0] = 1
                arr[i-1]= 1
                m=0
                n=1
                while n < i-1:
                    arr[n]=last[m]+last[n]
                    m+=1
                    n+=1
                pascal.append(arr)
            i+=1
        return pascal