class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
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
        return False