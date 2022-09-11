class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # The Optimal Solution, using XOR bitwise operator
        # Time Complexity : O(n) 
        # Space Complexity: O(1)
        output = 0
        
        for num in nums:
            output = output ^ num
            print(output ^ num)
        return output
        
        
        # It's working Solution, but not Effecient
        # Time Complexity : O(n) 
        # Space Complexity: O(n)
        """
        hashSet = set()
        for num in nums:
            if num in hashSet:
                hashSet.remove(num)
            else:
                hashSet.add(num)
        
        return hashSet.pop()
        """