class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """hash_map = {}
        for index, value in enumerate(nums1):
            
            hash_map[value] = index
        
        
        result = []
        
        for i in range(len(nums2)):
            if nums2[i] in hash_map:
                if i+1 == len(nums2):
                    result.insert(hash_map[nums2[i]], -1)
                    break
                if nums2[i] < nums2[i+1]:
                    result.insert(hash_map[nums2[i]], nums2[i+1])
                else:
                    result.insert(hash_map[nums2[i]], -1)
        return result"""
        

        """ans = list()
        nums1_map = {}
        j = 0
        
        for index, item in enumerate(nums1):
            nums1_map[item] = index

        found = False
        i = 0 
        while i < len(nums2):
            if nums2[i] in nums1_map:
                j = i+1
                while j < len(nums2):
                    if nums2[i] < nums2[j] and j != len(nums2):
                        ans[nums1_map[nums2[i]]] = nums2[j]
                        found = True
                        break
                    j += 1
                if found == False:
                    ans[nums1_map[nums2[i]]] = -1
            found = False
            i += 1"""
            
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

            
                
