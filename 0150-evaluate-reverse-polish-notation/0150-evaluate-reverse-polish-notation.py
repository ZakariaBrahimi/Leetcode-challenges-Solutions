import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Time  Complexity: O(n), n is the length of tokens array
        # Space Complexity: O(1)
        
        stack = []
        operations = {
            '*': operator.mul,  # Multiplication
            '+': operator.add,  # Addition
            '-': operator.sub,  # Subtraction
            '/': operator.truediv  # Division (true division)
        }

        for token in tokens:
            # If token is an operator, pop two operands and apply the operation
            if token in operations:
                second_integer = int(stack.pop())
                first_integer = int(stack.pop())
                
                # Perform the operation and truncate towards zero for division
                if token == '/':
                    operation_result = int(first_integer / second_integer)
                else:
                    operation_result = operations[token](first_integer, second_integer)
                
                stack.append(operation_result)
            else:
                # If token is a number, push it to the stack
                stack.append(int(token))

        return stack[0]  # The result will be the only item left in the stack
