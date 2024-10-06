# Problem Name: 14. Longest Common Prefix
# Problem Link: https://leetcode.com/problems/longest-common-prefix/description/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        j = 0
        returnStr = ""

        if(len(strs) == 1):
            return strs[0]

        while len(strs) > i + 1:
            if len(strs[i]) > j and len(strs[i + 1]) > j and strs[i][j] == strs[i + 1][j]:
                i += 1
                if len(strs) <= i + 1:
                    returnStr += strs[i][j]
                    i = 0
                    j += 1
            else:
                break
        return returnStr
