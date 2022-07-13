class Solution(object):
    def removeDuplicates(self, s, k):
        stack = [] # stack of arrays [char, count]
        for char in s:
            if stack and char == stack[-1][0]:
                stack[-1][1] += 1
            else:
                stack.append([char, 1])
                
            if stack[-1][1] == k:
                stack.pop()
        
        result = ''
        for pair in stack:
            result += pair[0] * pair[1]
        
        return result
        