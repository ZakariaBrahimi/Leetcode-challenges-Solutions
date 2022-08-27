class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # 1. Initializing 2 pointer with 0 & char counter for s1
        
        # 2. Iterating through out the string until the right poniter reach the end of the given string
        
        # 3. Expanding the window until we find all chars on the created counter
        
        # 4. Shrinking the window until we reach the length of s1
        
        left, right = 0, len(s1) - 1
        charCounter = Counter(s1)
        
        while right < len(s2):
            currentWindowMap = Counter(s2[left:right+1])
            if charCounter == currentWindowMap:
                return True
            left  += 1
            right += 1
        return False
        
            
            
                
        