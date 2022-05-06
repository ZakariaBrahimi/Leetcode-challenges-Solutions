class Solution(object):
    def toValidString(self, s):
        
        for char in s:
            # To check if it's alphanumeric or not
                if not (ord('A') <= ord(char) <= ord('Z') or
                    ord('a') <= ord(char) <= ord('z') or
                    ord('0') <= ord(char) <= ord('9')
                    ):
                        s = s.replace(char, '')  
        return s.lower()

    def isPalindrome(self, s):
        new_s = self.toValidString(s)
        leftPointer = 0
        rightPointer = len(new_s) - 1
        while (leftPointer < rightPointer):
                if new_s[leftPointer] == new_s[rightPointer]:
                        leftPointer  += 1
                        rightPointer -= 1
                else:
                        return False
        return True
        