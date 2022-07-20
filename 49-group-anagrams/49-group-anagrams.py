class Solution(object):
    def groupAnagrams(self, strs):
        # We don't need for input validation
        # The given array should contains atleast one string
        # Each string could be an empty
        # strs[i] consists of lowercase English letters.
        
        result = []
        result_map = {}
        
        for string in strs:
            
            if tuple(sorted(string)) in result_map:
                result_map[tuple(sorted(string))].append(string)
            else:
                result_map[tuple(sorted(string))] = [string, ]
        
        for val in result_map.values():
            result.append(val)
            
        return result
            
        
            