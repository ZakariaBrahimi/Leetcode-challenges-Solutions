class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min_value = sys.maxsize

    def push(self, val):
        self.min_value = min(self.min_value, val)
        self.stack.append(val)
        

    def pop(self):
        if len(self.stack) != 0:
            self.stack.pop()

    def top(self):
        if len(self.stack) != 0:
            return self.stack[-1]

    def getMin(self):
        minn = sys.maxsize
        if len(self.stack) != 0:
            for item in self.stack:
                minn = min(minn, item)
            return minn

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()