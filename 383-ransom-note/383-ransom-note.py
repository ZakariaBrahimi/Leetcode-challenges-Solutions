class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        # Time Complexity : O(n+m), where n, m is the length of 'ransomNote' and 'magazine' strings
        # Space Complexity: O(m), where m is the 'magazine' string
        latters_counter = Counter(magazine)
        
        for latter in ransomNote:
            if latters_counter[latter] == 0 or latter not in latters_counter:
                return False
            latters_counter[latter] -= 1
        
        return True