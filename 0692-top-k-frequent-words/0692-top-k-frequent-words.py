import collections
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        """
        words = ["i","love","leetcode", "no", "i","love","coding", "no"], k = 2
        {
            i: 2
            love: 2
            no: 2
            leetcode: 1
            coding: 1
        }
        this is the target bucket = [i, love, no]
        """
        
        # Creating the HashMap: {word: count}
        hashMap = collections.Counter(words)
        # Creating buckets
        buckets = [[] for i in range(len(words))]
        
        # Filling those buckets
        # + Sort the words with the same frequency by their lexicographical order
        for key, val in hashMap.items():
            buckets[val].append(key)
        print(buckets)
        # Iterate throut out the buckets
        for bucket in buckets:
            bucket.sort()
        print(buckets)
        # return the result in descending order 
        result = []
        for bucket_number in range(len(buckets)-1, 0, -1):
            for word in buckets[bucket_number]:
                result.append(word)
                if len(result) == k: return result
