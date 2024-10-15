class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = [-1] * len(nums1)
        hashMap = { number: index for index, number in enumerate(nums1)  }
        stack = []

        for i in range(len(nums2)):
            current = nums2[i]
            
            while stack and stack[-1] < current:
                top = stack.pop()
                index = hashMap[top]
                ans[index] = current

            if current in hashMap:
                stack.append(current)
        return ans
