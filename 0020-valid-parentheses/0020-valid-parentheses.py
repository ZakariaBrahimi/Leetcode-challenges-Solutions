class Solution:
    def isValid(self, s: str) -> bool:
        # First Solution without using hashMap loos a bit longer and not beauty
        # Time  Complexity: O(n)
        # Space Complexity: O(n)
        """
        stack = []
        for parenthes in s:
            if stack and ((stack[-1] + parenthes == '()') or 
               (stack[-1] + parenthes == '[]') or
               (stack[-1] + parenthes == "{}")) :
               stack.pop()
            else:
                stack.append(parenthes)

        return True if not stack else False
        """

        # Second Solution using hashMap loos a bit pro and beauty
        # Time  Complexity: O(n)
        # Space Complexity: O(n)
        stack = []
        parenthesMap = {
            '(' : ')',
            '[' : ']',
            '{' : '}',
        }
        for parenthes in s:
            # If it's a closing parenthesis
            if parenthes not in parenthesMap:
                # Pop the stack and check if the top matches the corresponding opening parenthesis
                if stack and stack[-1] == parenthes:
                    stack.pop()
                else:
                    return False

            # It's an opening parenthesis, so push it onto the stack
            else:
                stack.append(parenthesMap[parenthes])

        return True if not stack else False
