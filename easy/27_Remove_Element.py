class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        next_valid=1
        leng=len(nums)
        for i in range(len(nums)):
            if nums[i] ==val:
                next_valid= len(nums)
                for j in range(i,len(nums)):
                    if nums[j] != val:
                        next_valid=j
                        break
                if next_valid != len(nums):
                    nums[i]=nums[next_valid]
                    nums[next_valid]=val
                else:
                    leng-=1
                print(next_valid)
                print(nums)
        return leng

#def removeElement(self, nums, val):
    #i = 0
    #for x in nums:
    #    if x != val:
    #        nums[i] = x
    #        i += 1
    #return i
                    