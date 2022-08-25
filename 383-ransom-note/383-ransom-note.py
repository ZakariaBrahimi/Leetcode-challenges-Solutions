class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        latters_counter = Counter(magazine)
        
        for latter in ransomNote:
            if latters_counter[latter] == 0 or latter not in latters_counter:
                return False
            latters_counter[latter] -= 1
        
        return True
    
    # {a:1, b:1} , magazine= aa
        