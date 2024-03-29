class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:        
        left, right = 0, len(s1) - 1
        charCounter = Counter(s1)
        
        while right < len(s2):
            currentWindowMap = Counter(s2[left:right+1])
            if charCounter == currentWindowMap:
                return True
            left  += 1
            right += 1
        return False
        
            
            
                
        