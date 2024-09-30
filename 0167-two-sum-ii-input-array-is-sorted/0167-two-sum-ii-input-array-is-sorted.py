class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Two Pointers Technique
        # Time  Complexity: O(n)
        # Space Complexity: O(1)

        start, end = 0, len(numbers) -1
        while start < end:
            result = numbers[start] + numbers[end]
            if result == target:
                return [start+1, end+1]
            elif result < target:
                start += 1
            else:
                end -= 1