# Problem Name: 242. Valid Anagram
# Problem Link: https://leetcode.com/problems/valid-anagram/description/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) == len(t)):
            dictionary = {}
            for curChar in s:
                if curChar in dictionary.keys():
                    dictionary[curChar] += 1
                else:
                    dictionary[curChar] = 1
            for curChar in t:
                if curChar in dictionary.keys():
                    dictionary[curChar] -= 1
                    if dictionary[curChar] == 0:
                        dictionary.pop(curChar)
                else:
                    return False
        else:
            return False
        
        return True
