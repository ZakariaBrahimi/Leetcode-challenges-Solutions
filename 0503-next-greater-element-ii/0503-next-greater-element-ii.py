class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # if nums[i] > stack[-1] 
            # stack.pop[-1]
            # stack.append(nums[i])
            # result[k] = nums[i]

            stack = []
            result = [-1] * len(nums)

            for i in range(len(nums)):
                current = nums[i]
                while stack and current > stack[-1][0]:
                    top_val, index = stack.pop()
                    result[index] = current

                # if not stack or current < stack[-1][0]:
                stack.append([current, i])


            for i in range(len(nums)):
                current = nums[i]
                while stack and current > stack[-1][0]:
                    top_val, index = stack.pop()
                    result[index] = current
                
                
            # nums = [1,2,3,4,3]
            # current = 3
            # stack = [(4,3), (3, 4)]
            # result = [2, 3, 4, -1, 4]

            

            return result
