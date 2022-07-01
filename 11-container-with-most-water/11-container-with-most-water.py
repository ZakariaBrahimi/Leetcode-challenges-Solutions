class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        maxWater = 0
        while left < right:
            if height[left] < height[right]:
                maxWater = max(height[left]*(right-left), maxWater)
                left += 1
                #right += 1
            else:
                maxWater = max(height[right]*(right-left), maxWater)
                right -= 1
        return maxWater