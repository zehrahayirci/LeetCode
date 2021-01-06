#Thankyou @Ethan_M for the clarifications.
#Sometimes, I think I am lacking basic English 

#Hi,it wants us to do 2 things:
#1.return the num of the elements without duplication
#2.if you return m at the first step,you need to make the first m number of nums[] to be those elements without duplication,and it doesn't matter what you leave beyond the returned length.

#for example,you in put {1,1,2,2,3,3,5}
#you need to return 4 and make this to {1,2,3,5,x,x,x}

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        newTail = 0

        for i in range(1, len(nums)):
            if nums[i] != nums[newTail]:
                newTail += 1
                nums[newTail] = nums[i]

        return newTail + 1
        
        