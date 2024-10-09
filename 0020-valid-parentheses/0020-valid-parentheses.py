class Solution:
    def isValid(self, s: str) -> bool:
        # stack = []
        # for parenthes in s:
        #     if stack and ((stack[-1] + parenthes == '()') or 
        #        (stack[-1] + parenthes == '[]') or
        #        (stack[-1] + parenthes == "{}")) :
        #        stack.pop()
        #     else:
        #         stack.append(parenthes)

        # return True if not stack else False
        
        stack = []
        parenthesMap = {
            '(' : ')',
            '[' : ']',
            '{' : '}',
        }
        for parenthes in s:
            # if it is closing parenthes
            if parenthes not in parenthesMap:
                if stack and stack[-1] == parenthes:
                    stack.pop()
                else:
                    return False

            # if it is openning parenthes
            if parenthes in parenthesMap:
                stack.append(parenthesMap[parenthes])

        return True if not stack else False
