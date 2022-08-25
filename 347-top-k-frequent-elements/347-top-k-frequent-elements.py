class Solution(object):
    def topKFrequent(self, nums, k):
        most_frequent_elements = []
        hashMap = Counter(nums)
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