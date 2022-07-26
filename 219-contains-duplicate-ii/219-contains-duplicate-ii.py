class Solution(object):
    """def containsNearbyDuplicate(self, nums, k):
        # {1:0, 0:1, 1:2, 1:3}, k = 1 ===>> True
        # {0:1, 1:2, }
        # count = 2
        
        hash_map = dict()
        count = 0
        
        for index, num in enumerate(nums):
            if count == 2:
                return True
            if k in hash_map:
                count += 1
                s = hash_map.pop(k, 0)
            hash_map[num] = index
        
        return False"""
    
    def containsNearbyDuplicate(self, nums, k):
	    index_dict = {}


	    for i, n in enumerate(nums):
		    if n in index_dict and i - index_dict[n] <= k:
			    return True

		    index_dict[n] = i

	    return False
                
        