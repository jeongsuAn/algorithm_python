class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        discriminant = 0
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i] == needle[discriminant]:
                index = i
                for j in range(len(needle)):
                    if haystack[index] != needle[j]:
                        break
                    if j == len(needle)-1:
                        return i
                    index+=1
        return -1
