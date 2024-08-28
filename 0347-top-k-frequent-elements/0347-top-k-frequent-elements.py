class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # Time Complexity : O(n)
        # Space Complexity: O(n)

        # Building the HashTable
        hashTable = dict()
        for number in nums:
            if number in hashTable:
                hashTable[number] += 1
            else:
                hashTable[number] = 1

        # Backet Sort Algorithm
        # Creating Buckts
        buckets = [[] for i in range(len(nums)+1)]
        # Filling backets
        for key, val in hashTable.items():
            buckets[val].append(key)
        
        # Getting the k most frequent elements by loopping descending 
        result = []
        for i in range(len(buckets)-1, 0, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k: return result