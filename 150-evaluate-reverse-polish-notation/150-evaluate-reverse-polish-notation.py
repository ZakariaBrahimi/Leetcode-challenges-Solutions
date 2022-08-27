class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Time copmlexity : O(n)
        # Space copmlexity: O(n)
        
        # 0. Declaring variables
        stack = []
        operations = {'+', '-', '*', '/'}
        
        # 1. Iterate through out the given array
        for item in tokens:
        # 2. Keep pushing to the stack until we reach one of operators
            if item not in operations:
                stack.append(int(item))
            else:
        # 3. Poping the last 2 pushed numbers and do the operation
                if item == '+':
                    left    = stack.pop()
                    right   = stack.pop()
                    newItem = left + right
        # 4. Re-pushing the result again
                    stack.append(newItem)
                if item == '-':
                    right   = stack.pop()
                    left    = stack.pop()
                    newItem = left - right
                    stack.append(newItem)
                if item == '*':
                    left    = stack.pop()
                    right   = stack.pop()
                    newItem = left * right
                    stack.append(newItem)
                if item == '/':
                    right   = stack.pop()
                    left    = stack.pop()
                    newItem = left / right
                    stack.append(int(newItem))
        
        # 5. If we reach the end of the given list push the last remaining elemnt from the stack and return it.
        return stack.pop()