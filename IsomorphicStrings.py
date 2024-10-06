# Problem Name: 205 Isomorphic Strings
# Problem List: https://leetcode.com/problems/isomorphic-strings/description/

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dictionary = {}
        listToCheckDoubleVals = []
        checkStr = ""
        for i in range(len(s)):
            dictionary[s[i]] = t[i]
        for i in dictionary.values():
            if i in listToCheckDoubleVals:
                return False
            else:
                listToCheckDoubleVals.append(i)
        for i in range(len(s)):
            checkStr += dictionary[s[i]]
        if checkStr == t:
            return True
        else:
            return False
