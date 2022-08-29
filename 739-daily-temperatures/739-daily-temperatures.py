class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack  = [] 
        result = [0]*len(temperatures)
        for index, temp in enumerate(temperatures):
            if not stack:
                stack.append([index, temp])
                continue
            while stack and temp > stack[-1][1]:
                i, element  = stack.pop()
                result[i]   = index - i
            stack.append([index, temp])

        return result
        