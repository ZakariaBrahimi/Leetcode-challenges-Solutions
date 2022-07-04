class Solution(object):
    def intersection(self, nums1, nums2):
        hashSet = set()
        result = list()
        for item in nums1:
            hashSet.add(item)
        
        for item in nums2:
            if item in hashSet and item not in result:
                result.append(item)

        return result
        