class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        char_dictionary = dict()
        for i in range(len(s)):
            if s[i] not in char_dictionary:
                char_dictionary[s[i]] = t[i]
            else:
                if char_dictionary[s[i]] != t[i]:
                    return False
        dictionary_value_list = []
        for key,value in char_dictionary.items():
            if value not in dictionary_value_list:
                dictionary_value_list.append(value)
            else: 
                return False
        return True