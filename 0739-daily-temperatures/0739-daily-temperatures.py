class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        temperatures = [73,74,75,71,69,72,76,73]
        enswer       = [1,  1, 4, 2, 1, 1, 0, 0]
        """
        # Initialize anwser array with 0 and length of temp array
        stack = []
        anwser = [0] * len(temperatures)
        # Loop tghrought out the array from the right to left
        for i in range(len(temperatures)):
            current = temperatures[i]
            while stack and current > stack[-1][0]:
                temp, index = stack.pop()
                anwser[index] =  i - index 
            
            stack.append([current, i])
                


        return anwser
        # if temp[i] < stack[-1] ===>
        #  append to stack and anwser[i] = j-i 

        # if temp[i] > stack[-1]
        # keep poping from stack and  anwser[i] = j-i 