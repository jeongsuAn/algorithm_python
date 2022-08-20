class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sLen = len(s)
        tLen = len(t)
        if sLen > tLen:
            return False
        tempSIndex = 0
        tempTIndex = 0
        while True:
            if sLen == tempSIndex:
                return True
            if tLen == tempTIndex:
                return False
            
            if s[tempSIndex] == t[tempTIndex] :
                tempSIndex += 1
                tempTIndex += 1
            else:
                tempTIndex += 1
            