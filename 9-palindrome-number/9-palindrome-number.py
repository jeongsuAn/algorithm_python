class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False;
        forwardNumString = list(str(x))
        forwardNumStringLen = len(forwardNumString)
        for i in forwardNumString:
            if i != forwardNumString[forwardNumStringLen-1]:
                return False
            forwardNumStringLen = forwardNumStringLen-1
        return True
        
        
        