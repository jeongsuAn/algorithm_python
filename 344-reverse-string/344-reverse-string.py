class Solution:
    def reverseString(self, s: List[str]) -> None:
        
        list_len = len(s)
        temp_index = list_len-1 # the last index in list s
        
        for idx in range(int(list_len/2)):
            temp_str = s[temp_index]
            s[temp_index] = s[idx]
            s[idx] = temp_str
            temp_index -= 1
            