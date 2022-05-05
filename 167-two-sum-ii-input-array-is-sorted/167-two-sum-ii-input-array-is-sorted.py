class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        if (len(numbers) == 2):
                return [1, 2]
        leftPointer = 0 
        rightPointer = len(numbers) - 1 
        while (leftPointer < rightPointer):
            sum = numbers[leftPointer] + numbers[rightPointer]
            if (sum == target):
                return [leftPointer+1, rightPointer+1] # because of we should return 1-index array
            elif (sum < target):
                leftPointer += 1
            else:
                rightPointer -= 1