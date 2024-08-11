class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """

        """
        # Time Complexity: O(n)
        # Space Comlexity: O(n)
        # n: is the length of word1
        word1 = ["ab", "c"], word2 = ["a", "bc"]
        looping and concatinate ==>> word1 = abc, word2= abc
        if len(word1) !== len(word2): return False
        for i in range(len(word1)):
            if word1[i] !== word2[i]: return False

        return True
        """
        
        word1concatinated = ''
        word2concatinated = ''

        for string in word1:
            word1concatinated += string
        for string in word2:
            word2concatinated += string

        if len(word1concatinated) != len(word2concatinated): return False
        
        for i in range(len(word1concatinated)):
            if word1concatinated[i] != word2concatinated[i]: return False
        
        return True
