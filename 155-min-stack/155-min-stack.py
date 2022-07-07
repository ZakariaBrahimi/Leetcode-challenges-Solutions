class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min_value = float('inf')
        self.min_values_stack = []

    def push(self, val):
        self.stack.append(val)
        if len(self.min_values_stack) == 0:
            self.min_values_stack.append(val)
        else:
            val = min(val, self.min_values_stack[-1])
            self.min_values_stack.append(val)

    def pop(self):
        self.stack.pop()
        self.min_values_stack.pop()
                
            

    def top(self):
        if len(self.stack) != 0:
            return self.stack[-1]

    def getMin(self):
        #if not self.min_values_stack:
        return self.min_values_stack[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()