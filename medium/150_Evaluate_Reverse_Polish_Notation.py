class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for item in tokens:
            if item =="+":
                stack.append(stack.pop() + stack.pop())
                
            elif item =="-":
                stack.append(stack.pop(-2) - stack.pop())
                
            elif item =="/":
                stack.append(int(stack.pop(-2) / stack.pop()))
                
            elif item =="*":
                stack.append(stack.pop() * stack.pop())
                
            else:
                stack.append(int(item))
            #print(stack)
        return stack[0]
                
                