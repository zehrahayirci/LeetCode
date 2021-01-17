class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n==1:
            return "1"
        else:
            return self.step(self.countAndSay(n-1))
        
        
    def step(self, input_s):   
        cur_cnt = 0 
        cur_char =None 
        output_s=''
        for c in input_s:
            if c==cur_char:
                cur_cnt+=1
            else:
                if cur_char : 
                    output_s+= "{}{}".format(cur_cnt, cur_char)
                cur_char = c
                cur_cnt = 1
                
        output_s+= "{}{}".format(cur_cnt, cur_char)
        return output_s