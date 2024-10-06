# Problem Name: 67. Add Binary
# Problem Link: https://leetcode.com/problems/add-binary/description/

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
