class Solution(object):
    def removeDuplicates(self, s):
        """
        s = aaca
        stack = [a]
        if stack is not empty and s[i] == stack[-1] 
            result = s[0:i] + s[i+1:]
            stack.pop()
            
            
        stack.append(s[i])
        """
        stack = []
        result = ""
        for i in range(len(s)):
            if  stack and s[i] == stack[-1]:
                stack.pop()
                continue
            stack.append(s[i])
        for char in stack:
            result += char
        return result