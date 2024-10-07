class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for parenthes in s:
            if stack and ((stack[-1] + parenthes == '()') or 
               (stack[-1] + parenthes == '[]') or
               (stack[-1] + parenthes == "{}")) :
               stack.pop()
            else:
                stack.append(parenthes)

        return True if not stack else False