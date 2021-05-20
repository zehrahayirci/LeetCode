#Binary Search
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:        
        left, right = 0, len(arr) - k
        while left < right:
            mid = (left + right) // 2
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid
        return arr[left:left + k]


#My TimeLimit BruteForce
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        uzakliklar = {}
        res =[]
        #if len(arr) <2:
        #    return arr
        for j,item in enumerate(arr):
            uzakliklar[j] = abs(item - x)
        #print(uzakliklar)
        for i in range(k):
            
            a = min(uzakliklar.values())
            #print(a)
            kk = (list(uzakliklar.keys())[list(uzakliklar.values()).index(a)])  # Prints george
            #print(arr[kk])
            res.append(arr[kk])
            uzakliklar.pop(kk)
        return sorted(res)