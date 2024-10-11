import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1: return int(tokens[0])
        stack = []
        # operations = {'*': *, '+': +, '-': -, '/': /}
        operations = {
            '*': operator.mul,  # Multiplication
            '+': operator.add,  # Addition
            '-': operator.sub,  # Subtraction
            '/': operator.truediv  # Division (true division)
        }
        operation_result = 0
        for token in tokens:
            # if token == operation --> pop twice
            if token in operations.keys():
                second_integer = int(stack.pop())
                first_integer  = int(stack.pop())
                operation_result = int(operations[token](first_integer, second_integer))
                stack.append(operation_result)
            # if token == integer   --> append to stack
            else:
                stack.append(int(token))
        print(operation_result)
        return operation_result