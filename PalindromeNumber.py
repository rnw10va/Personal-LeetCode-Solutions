#Problem Name: 9. Palindrome Number
#Problem Link: https://leetcode.com/problems/palindrome-number/description/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = x
        reverseX = 0
        while y > 0:
            singleDigit = y % 10
            reverseX = reverseX * 10 + singleDigit
            y //= 10
        return x == reverseX
