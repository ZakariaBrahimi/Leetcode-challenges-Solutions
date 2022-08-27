class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Time Complexity : O(n), n= length of the given string
        # Space Complexity: O(n)
        # Valid Sub-string: (substring.length) - (number of leteres that repeated the most) <= k
        charCounter = {}
        left, right = 0, 0
        window = 0
        result = 0 
        
        # 1. iterate through out the string until the right pointer reach the end of the string
        while right < len(s):
        # 2. Expand the window by one then shift the right pointer, until we reach the valid substring
            window += 1
            charCounter[s[right]] = 1 + charCounter.get(s[right], 0) 
            right  += 1
            # if the sub-string is valid
            if (len(s[left:right]) - max(charCounter.values())) <= k: 
                result = max(result, window)
            # if the sub-string is not valid
            else:
                # Keep shift the left pointer until we find the valid sub-string and than shift the right pointer
                while ((len(s[left:right]) - max(charCounter.values())) > k):
                    window -= 1
                    charCounter[s[left]] -= 1
                    left   += 1
        
        # 3. returning the max length of the same characters
        return result