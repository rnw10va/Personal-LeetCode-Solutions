# Problem Name: 290. Word Pattern
# Problem Link: https://leetcode.com/problems/word-pattern/description/

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dictionary = {}
        sStringSplit = s.split()
        if len(sStringSplit) != len(pattern):
            return False
        else:
            for i in range(len(pattern)):
                if pattern[i] in dictionary.keys():
                    if dictionary[pattern[i]] != sStringSplit[i]:
                        return False
                elif sStringSplit[i] in dictionary.values():
                    return False
                else:
                    dictionary[pattern[i]] = sStringSplit[i]
        return True
