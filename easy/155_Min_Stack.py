class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.mystack = []
        

    def push(self, val: int) -> None:
        self.mystack.append(val)

    def pop(self) -> None:
        self.mystack = self.mystack[0:-1]

    def top(self) -> int:
        return self.mystack[-1]

    def getMin(self) -> int:
        return min(self.mystack)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()