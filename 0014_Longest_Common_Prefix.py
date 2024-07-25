class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        index = -1

        flag = True
        while flag:
            index += 1

            if index < len(strs[0]):
                base = strs[0][index]
            else:
                break
            
            for s in strs[1:]:
                if index >= len(s) or s[index] != base:
                    flag = False
                    break
        return strs[0][:index]
