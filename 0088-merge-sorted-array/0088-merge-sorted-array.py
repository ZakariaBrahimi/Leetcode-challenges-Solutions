class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        nums1 = [], langth of m
        nums2 = [], length of n
        - both arrays are sorted in non-decreasing order

        task: merge both of the arrays in the same order
        return: nums1(no extra memory space)
        constraints:
            - nums1.length == m + n | nums2.length == n
            - 0 <= m, n <= 200 |1 <= m + n <= 200
            - arrays number could be negative and positive integers

        edge cases:
            - m=0 => return nums2 | n=0 => return nums1

        brute force solution: using extra memory space
        better solution: using three pointers
        """
        # Time Complexity : O(n)
        # Space Complexity: O(1)
        pointer1, pointer2, pointer3 = m-1, n-1, m+n-1

        while(pointer1+1 > 0 and pointer2+1 > 0):
            if nums1[pointer1] >= nums2[pointer2]:
                nums1[pointer3] = nums1[pointer1]
                pointer1 -= 1  
            else:
                nums1[pointer3] = nums2[pointer2]
                pointer2 -= 1
            pointer3 -= 1
        if pointer2+1 > 0:
            nums1[:pointer2+1] = nums2[:pointer2+1]
        