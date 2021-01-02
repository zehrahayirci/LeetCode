def romanToInt( s):
    """
    :type s: str
    :rtype: int
    """
    
    Romans={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    number=0
    if len(s) == 1 :
        number = Romans[s[0]]
    else:
        for i in range (0,len(s)-1):
            prev_value=Romans[s[i-1]]
            value=Romans[s[i]]
            next_value=Romans[s[i+1]]
            print(i,value,next_value)
            if value < next_value:
                number-=value
            else:
                number+=value
            print(number)

        
        number+=Romans[s[-1]]
    return number

print(romanToInt("MCMXCIV"))