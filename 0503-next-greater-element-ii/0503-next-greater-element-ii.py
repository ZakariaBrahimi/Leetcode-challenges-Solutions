class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # Solved Using: Monotonic Stack Data Structure
        # Time  Complexity: O(n)
        # Space Complexity: O(n)

            stack = []
            result = [-1] * len(nums)

            for i in range(len(nums)):
                current = nums[i]
                while stack and current > stack[-1][0]:
                    top_val, index = stack.pop()
                    result[index] = current

                stack.append([current, i])

            for i in range(len(nums)):
                current = nums[i]
                while stack and current > stack[-1][0]:
                    top_val, index = stack.pop()
                    result[index] = current
                
            return result
