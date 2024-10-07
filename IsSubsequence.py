# Problem Name: 392. Is Subsequence
# Problem Link: https://leetcode.com/problems/is-subsequence/description/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) <= len(t):
            i = 0
            j = 0
            while i < len(t) and j < len(s):
                if t[i] == s[j]:
                    j+=1
                i+=1
            if j == len(s):
                return True
            else:
                return False

        else:
            return False
