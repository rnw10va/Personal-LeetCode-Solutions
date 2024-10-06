# Problem Name: 28. Find the Index of the First Occurrence in a String
# Problem Link: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(1 + len(haystack) - len(needle)):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
