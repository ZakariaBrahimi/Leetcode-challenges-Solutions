class Solution(object):
    def topKFrequent(self, nums, k):
        """
        # Time Complexity : O(n*k), linear Time
        # Space Complexity: O(k+n),
        # where n is the length of hashMap, 
        # worst case nums array contains only different numbers [1,3,4,9,7,6,5], so k could be 7
        most_frequent_elements = []
        hashMap = Counter(nums) # O(n) to build the map
        current_val = -1
        while k!=0:
            for key, value in hashMap.items():
                if value > current_val:
                    current_val = value
                    current_key = key
            most_frequent_elements.append(current_key)
            hashMap[current_key] = -1
            k -= 1
            current_val = -1
        
        return most_frequent_elements
        """
        
        # Bucket Sorting Approach
        # Time Complexity : O()
        # Space Complexity: O()
        most_frequent_elements = list()
        buckets = [[] for i in range(len(nums) + 1)]
        
        # 1. Constructing the Map
        hashMap = {}
        for num in nums:
            if num in hashMap:
                hashMap[num] += 1
            else:
                hashMap[num] = 1
        

        # 2. Filling The bucket where the array index == frequent of numbers
        for key, value in hashMap.items():
            buckets[value].append(key)
        
        # 4. poping the last k elements from the bucket array
        for bucket_number in range(len(buckets)-1, 0, -1):
            for num in buckets[bucket_number]:
                most_frequent_elements.append(num)
        # 3. Returning
                if k == len(most_frequent_elements):
                    return most_frequent_elements
                
        
        return most_frequent_elements