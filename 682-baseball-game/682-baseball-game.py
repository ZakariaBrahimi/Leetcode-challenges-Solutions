class Solution(object):
    def calPoints(self, ops):
        stack = []
        for char in ops:
            try:
                if isinstance(int(char), int):
                    stack.append(int(char))
            except:
                if stack and char == 'C':
                    stack.pop()
                if stack and char == 'D':
                    new_value = stack[-1]*2
                    stack.append(new_value)
                if len(stack) > 1 and char == '+':
                    new_value = stack[-1] + stack[-2]
                    stack.append(new_value)
        
        result = 0
        for num in stack:
            result += num
            
        return result
        