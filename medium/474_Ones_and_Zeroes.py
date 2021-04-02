class Solution(object):
    def findMaxForm(self, strs, m, n):
        dp = [[ 0 ] * (n+1) for _ in range(m+1)]
        for s in strs:
            zeros, ones = s.count("0"), s.count("1")
            for i in range(m, zeros - 1, -1):
                for j in range(n, ones - 1, -1):
                    dp[i][j] = max( 1 + dp[i - zeros][j- ones], dp[i][j] )
            # print(dp)
        return dp[-1][-1]
    '''
    def subset_sum(self,numbers,target,res, partial=[]):
        s = 0
        for item in partial:
            s+= item[0]

        # check if the partial sum is equals to target
        if s <= target:
            res.append(partial) 
        if s > target:
            return  # if we reach the number why bother to continue

        for i in range(len(numbers)):
            n = numbers[i]
            remaining = numbers[i + 1:]
            self.subset_sum(remaining, target, res,partial + [n])
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        ones = []
        zeros = []
        numbers=[]
        for s in strs:
            zero=0
            one=0
            for c in s:
                if c =='0':
                    zero+=1
                else:
                    one+=1
            numbers.append([one,zero])
            ones.append(one)
            zeros.append(zero)
        res_one =[]
        self.subset_sum(numbers, n, res_one,partial=[])
        max_len = 0
        for item in res_one:
            sum_zero=0
            for i in item:
                sum_zero+=i[1]
            if sum_zero <= m and len(item)>max_len:
                max_len=len(item)
        return max_len
    '''
        
        