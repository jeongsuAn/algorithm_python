class Solution:
    def isPalindrome(self, s: str) -> bool:
        plain_str = []
        s = s.lower()
        for s_char in s:
            if (s_char>='a' and s_char<='z') or (s_char>='0' and s_char<='9'):
                plain_str.append(s_char)
                
        if len(plain_str)%2 == 1:
            if plain_str[0:int(len(plain_str)/2):1] == plain_str[-1:int(len(plain_str)/2):-1]:
                return True
            
        else: # len(plain_str)%2 == 0
            if plain_str[0:int(len(plain_str)/2):1] == plain_str[-1:int(len(plain_str)/2)-1:-1]:
                return True
            
        return False