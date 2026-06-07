"""
Problem Name: 67. Add Binary
Problem Link: https://leetcode.com/problems/add-binary/description/
Problem Description:

Given two binary strings a and b, return their sum as a binary string.

Example 1:
Input: a = "11", b = "1"
Output: "100"

Example 2:
Input: a = "1010", b = "1011"
Output: "10101"

Constraints:
    1 <= a.length, b.length <= 104
    a and b consist only of '0' or '1' characters.
    Each string does not contain leading zeros except for the zero itself.
"""

#My Solution
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        returnStr = ''
        carryVal = 0
        a = a[::-1]
        b = b[::-1]
        while len(a) > 0 or len(b) > 0 or carryVal > 0:
            aVal = bVal = '0'
            if len(a) > 0:
                aVal = a[0]
                a = a[1:]
            if len(b) > 0:
                bVal = b[0]
                b = b[1:]
            digSolVal = int(aVal)+int(bVal)+carryVal
            if digSolVal >= 2:
                carryVal = 1
            else:
                carryVal = 0
            returnStr = str(digSolVal % 2) + returnStr
        return returnStr