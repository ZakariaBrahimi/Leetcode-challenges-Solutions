class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
	    index_dict = {}

	    for i, n in enumerate(nums):
		    if n in index_dict and i - index_dict[n] <= k:
			    return True

		    index_dict[n] = i

	    return False