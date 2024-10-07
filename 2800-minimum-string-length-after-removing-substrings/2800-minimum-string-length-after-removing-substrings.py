class Solution:
    def minLength(self, s: str) -> int:
        """
            ABFCACDB
            sliding widow of length 2 
            wind1 = "1B" or wind2 = "CD"

            new_string = string
            looping throight the string where i == 0 and stops when i < len(string) - 1:
                if string[i] + string[i+1] == "AB" or "CD":
                    new_string = string[i+2:]
                else: i += 1

            return len(new_string) 
        """
        stack = []
        for char in s:
            # if stack is empty
            if not stack or not ((stack[-1] + char == 'AB') or (stack[-1] + char == 'CD')):
                stack.append(char)
            else:
                stack.pop()

        return len(stack)