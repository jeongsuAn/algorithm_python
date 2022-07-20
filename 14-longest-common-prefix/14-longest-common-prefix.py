class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        result = strs[0]
        equal_index = len(strs[0])
        if equal_index == 0:
            return ""

        if len(strs) == 1:
            return strs[0]
        
        for i in range(len(strs)):
            for j in range(min(len(strs[i]),equal_index)):
                if strs[0][j] != strs[i][j]:
                    equal_index = j;
                    if j == 0:
                        return ""
                    break
        return strs[0][:equal_index]