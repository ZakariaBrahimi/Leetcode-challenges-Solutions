class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charCounter = {}
        left, right = 0, 0
        window = 0
        result = 0
        
        # Valid Sub-string: (substring.length) - (number of leteres that repeated the most) <= k 
        
        # 1. iterate through out the string until right pointer reach the end of the string
        while right < len(s):
        # 3. Expand the window by one then shift the right pointer, until we reach the valid substring
            window += 1
            charCounter[s[right]] = 1 + charCounter.get(s[right], 0)
            #isValid = len(s[left:right+1]) - max(charCounter.values()) <= k
            right  += 1
            if (len(s[left:right]) - max(charCounter.values())) <= k:
                result = max(result, window)
            else:
                while not ((len(s[left:right]) - max(charCounter.values())) <= k):
                    window -= 1
                    charCounter[s[left]] -= 1
                    left   += 1
        
        # 3. returning the max length of the same characters
        return result