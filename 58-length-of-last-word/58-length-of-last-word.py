class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.rstrip()
        index = -1
        s_len = len(s)
        while True:
            if s_len >= abs(index) and s[index] != " ":
                index -= 1
            else:
                return -index-1