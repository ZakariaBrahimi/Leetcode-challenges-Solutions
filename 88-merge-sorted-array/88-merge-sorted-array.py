class Solution(object):
    def merge(self, nums1, m, nums2, n):

        p1 = m-1
        p2 = n-1
        last = m+n-1
        while p2 +1> 0 and p1 +1> 0:
            if nums1[p1] < nums2[p2]:
                nums1[last] = nums2[p2]
                p2 -= 1
            else:
                nums1[last] = nums1[p1]
                p1 -= 1
            last -= 1
        while p2+1 >0:
            nums1[last] = nums2[p2]
            p2 -= 1
            last -= 1
        return nums1