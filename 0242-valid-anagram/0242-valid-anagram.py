from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Time Complexity : O(n+m)
        # Space Complexity: O(n+m)
        if (len(s) != len(t)): return False
        hashTableS = Counter(s)
        hashTableT = Counter(t)
        for key in hashTableS.keys():
            if (key not in hashTableT or hashTableT[key] != hashTableS[key]):
                return False
        return True
        """
            s = "anagram", t = "nagaram"
            hashTableS = {
                a: 3,
                n: 1,
                g: 1,
                r: 1,
                m: 1
            }
            hashTableT = {
                n: 1,
                a: 3,
                g: 1,
                r: 1,
                m: 1
            }

            
        """