class Solution:
    def minLength(self, s: str) -> int:
        # Time  Complexity: O(n)
        # Space Complexity: O(n), in worst case, there is no AB and CD
        stack = []
        for char in s: # O(n), n is the length of string ns
            # if stack is empty and there are no AB or CD
            if not stack or not ((stack[-1] + char == 'AB') or (stack[-1] + char == 'CD')):
                stack.append(char) # O(1)
            else:
                stack.pop() # O(1)

        return len(stack)