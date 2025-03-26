import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_lower = s.lower()
        num_and_alpabet_pattern = "[a-zA-Z0-9]"
        list_s = re.findall(num_and_alpabet_pattern, s_lower)
        
        reverse_list_s = list_s.copy()
        reverse_list_s.reverse()

        if reverse_list_s == list_s: 
            return True
        else:
            return False
        