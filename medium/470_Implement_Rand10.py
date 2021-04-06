 

# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7
class Solution(object):
    def rand10(self):
        """
        :rtype: int
        """
    
        rand40=40
        while rand40>=40:
            rand40=(rand7()-1)*7+rand7()-1
        return rand40%10+1
        
        
        

'''
This is not working because adding two random numbers wont give you a random distribution for the third

# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7
    # 11 12 13 14 15 16 17
    # 11 12 13 14 15 16 27
    # 11 12 13 14 15 16 37
    # 11 12 13 14 15 16 47
    # 11 12 13 14 15 16 57
    # 61 62 63 64 65 66 67
    # 71 72 73 74 75 76 77
class Solution(object):
    def rand10(self):
        """
        :rtype: int
        """
        d = {1:[11,12,13,14],2:[15,16,17,21],3:[22,23,24,25], 4:[26,27,31,32],
            5:[33,34,35,36],6:[37,41,42,43],7:[44,45,46,47], 8:[51,52,53,54], 9:[55,56,57,61],10:[62,63,64,65]}
        a = rand7()
        b = rand7()
        while(a == 7):
            a = rand7()
        if a == 6:
            while(b == 7 or b==6):
                b = rand7()
        s =int(''+str(a)+str(b))
        for key in d:
            if s in d[key]:
                return key
'''