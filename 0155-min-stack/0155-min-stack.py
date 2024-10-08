class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.minStack.append(val)

        elif val > self.minStack[-1]:
            self.minStack.append(self.minStack[-1])
        else:
            self.minStack.append(val)
        
        self.stack.append(val)


    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        return

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()