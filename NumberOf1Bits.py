# Problem Name: 191. Number of 1 Bits
# Problem Link: https://leetcode.com/problems/number-of-1-bits/description/

class Solution:
    def hammingWeight(self, n: int) -> int:
        output = 0
        while n != 0:
            if n & 1:
                output += 1
            n = n >> 1
        return output
