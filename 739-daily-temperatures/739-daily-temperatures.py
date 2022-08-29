class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Time  Complexity: O(n)
        # Space Complexity: O(n)
        stack  = [] 
        result = [0]*len(temperatures)
        
        for index, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                i, element  = stack.pop()
                result[i]   = index - i
            stack.append([index, temp])

        return result