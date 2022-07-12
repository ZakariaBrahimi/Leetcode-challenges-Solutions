class Solution(object):
    def nextGreaterElement(self, nums1, nums2):            
        """
        nums1_hash_map = {value:index for index, value in enumerate(nums1) }
        result = [-1] * len(nums1)
        for i in range(len(nums2)):
            if nums2[i] in nums1_hash_map:
                for j in range(i+1, len(nums2)):
                    if nums2[i] < nums2[j]:
                        index = nums1_hash_map[nums2[i]]
                        value = nums2[j]
                        result[index] = value
                        break
        return result
        """
        stack = []
        nums1_hash_map = {value:index for index, value in enumerate(nums1) }
        result = [-1] * len(nums1)
        
        for i in range(len(nums2)):
            current = nums2[i]
            while stack and current > stack[-1]:
                val = stack.pop()
                index = nums1_hash_map[val]
                result[index] = current
            if current in nums1_hash_map:
                stack.append(current)
        
        return result