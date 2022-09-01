class Solution:
    def romanToInt(self, s: str) -> int:
        """
        - Example 1:
            MCMXCIV -> 1994
            M > C -> 1000
            C < M -> M - C = 1000 - 100 = 900
            X < C -> C - X = 100  - 10  = 90
            I < V -> V - I =  5   - 1   = 4
            result = 1000 + 900 + 90 + 4 = 1994
        
        - Example 2:
            LVIII -> 58
            L > V -> 50
            V > I -> 5
            I = I = 1*3 = 3
            result = 50 + 5 + 3 = 58
            
        Note: Using hashMap to store all 7 roman Symbols {Roman_symbol: Integer_value}
              -> for constant lookups
              
        1. Iterate over the given string
        
        2. If the current char is greater or equal than the next
            -> add the current value to the result
            -> increment the counter by 1
        
        3. If current char is less than the next
            -> substract the next by the current
            -> add the value to the result
            -> increment the counter by 2
        
        4. Return the result
        
        """
        # Time Copmlexity : O(n)
        # Space Complexity: O(1), 
        values     = [1, 5, 10, 50, 100, 500, 1000]
        symbols    = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        symbolsMap = {symbols[i]:values[i] for i in range(len(values))} # Space: O(7) -> O(1)
        result     = 0 
        i = 0
        
        while i < len(s):
            curent_symbol = s[i]
            if i != len(s)-1: 
                next_symbol = s[i+1]
                if symbolsMap[curent_symbol] >= symbolsMap[next_symbol]:
                    result += symbolsMap[curent_symbol]
                    i += 1
                else:
                    result += symbolsMap[next_symbol] - symbolsMap[curent_symbol]
                    i += 2
            else:
                result += symbolsMap[curent_symbol]
                i += 1
        return result     