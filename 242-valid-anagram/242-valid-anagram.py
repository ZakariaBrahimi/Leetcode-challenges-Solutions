class Solution(object):
    def isAnagram(self, s, t):
        """
        t_hashMap, s_hashMap = {}, {}
        if len(s) != len(t):
            return False
        for letter in s:
                if letter in s_hashMap:
                        s_hashMap[letter] += 1
                else:
                        s_hashMap[letter] = 1
        
        for letter in t:
                if letter in t_hashMap:
                        t_hashMap[letter] += 1
                else:
                        t_hashMap[letter] = 1
        
        if s_hashMap == t_hashMap:
                return True
        return False"""
        
        
        
        
        
        
        
        
        
        
        
        
        s_map = collections.Counter(s)
        t_map = collections.Counter(t)
        
        if s_map == t_map:
            return True
        
        return False