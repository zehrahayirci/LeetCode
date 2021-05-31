class Solution:
    def fib(self, n: int) -> int:
        #fib(0) = 0
        #fib(1) = 1
        arr = [0,1]
        for i in range(n):
            arr[0],arr[1] = arr[1],arr[0]+arr[1]
        #print(arr)
        return arr[0]