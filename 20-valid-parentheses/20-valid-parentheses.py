class Solution:
    def isValid(self, s):
        # This is another similair solution that I do'nt knwo where is the problem exactly
        """
        ()[{}]

        stack = 
        ")(){}"
        """"""
        charMap = {
            '(' : ')',
            '[' : ']',
            '{' : '}',
        }
        Map = { ')':"(" ,"]":"[" ,"}":"{" }
        stack = []
        if len(s)==1:return False 
        
        for bracket in s:
            if bracket in charMap: #means check if it's opening bracket
                stack.append(charMap[bracket])
            if bracket not in charMap and len(stack) != 0: #means check if it's closing bracket
                if bracket == stack[-1]:
                    stack.pop()
                else: return False

        return True if len(stack) == 0 else False
    
    
    """
        Map = { ')':"(" ,"]":"[" ,"}":"{" }
        stack = []
        
        for c in s:
            if c not in Map:
                stack.append(c)
                continue    
            if not stack or stack[-1] != Map[c]:
                return False
            stack.pop()
            
        return not stack

                    
                    
                    

