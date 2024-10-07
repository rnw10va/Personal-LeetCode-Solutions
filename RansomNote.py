# Problem Name: 383. Ransom Note
# Problem Link: https://leetcode.com/problems/ransom-note/description/

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazineHashMap = {}
        for curChar in magazine:
            if curChar in magazineHashMap:
                magazineHashMap[curChar] += 1
            else:
                magazineHashMap[curChar] = 1

        for curChar in ransomNote:
            if curChar in magazineHashMap:
                magazineHashMap[curChar] -= 1
                if magazineHashMap[curChar] < 0:
                    return False
            else:
                return False
        return True
