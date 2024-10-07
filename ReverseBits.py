# Problem Name: 190. Reverse bits
# Problem Link: https://leetcode.com/problems/reverse-bits/description/

class Solution:
    def reverseBits(self, n: int) -> int:
        binaryReverse = n & 1

        for i in range(1,32):
            binaryReverse = (binaryReverse << 1) + ((n >> i) & 1)
        return binaryReverse
