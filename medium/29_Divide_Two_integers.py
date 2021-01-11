class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        div=0
        flag= 1
        if divisor < 0:
            flag = flag * -1
            divisor = abs(divisor)
        if dividend < 0:
            flag = flag * -1
            dividend = abs(dividend) 
        if divisor == 1:
            result =  dividend * flag
            return min(max(-2147483648, result), 2147483647)
        
        real_divisor = divisor
        while dividend>=real_divisor:
            cur_d = 1
            divisor = real_divisor

            while dividend>=divisor:
                div+=cur_d
                dividend-=divisor

                cur_d = cur_d * divisor
                divisor = divisor*divisor
                

        result = div*flag
        return min(max(-2147483648, result), 2147483647)
        