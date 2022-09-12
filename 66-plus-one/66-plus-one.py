class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Time Complexity : O(n)
        # Space Complexity: O(1)
        i = -1
        s = True
        while s:
            if i >= -len(digits):
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i] += 1
                    s = False
            else:
                digits.insert(0, 1)
                s = False
            i -= 1
        
        return digits
        
        """
        Edge Cases:
            -> [1,9,9] -> [2,0,0]
            -> [9,9,9] -> [1,0,0,0]
        
        [1,2,3]
        -> '123' -> 123 -> 123 + 1 = 124 -> '124' -> [1,2,4]
        """
        # Iintuitive Solution using Python built-in functions
        """
        toString = ''
        for num in digits:
            toString += str(num)
        toString = str(int(toString) + 1)
        
        digits = []
        for num_str in toString:
            digits.append(int(num_str))
        
        return digits
        """
        