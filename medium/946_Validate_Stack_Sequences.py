class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        pop_array = []
        
        i=0
        j=0
        while len(pushed)>-1:
            while(len(pop_array)>0 and pop_array[-1]==popped[0]):
                pop_array.pop(-1)
                popped.pop(0)
            if len(pushed)==0 and len(popped)>0:
                return False
            elif len(pushed) == 0:
                return True
            pop_array.append(pushed[0])
            pushed.pop(0)
        return True
        