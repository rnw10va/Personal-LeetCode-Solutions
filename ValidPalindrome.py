# Problem Name: 125. Valid Palindrome
# Problem Link: https://leetcode.com/problems/valid-palindrome/description/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        iterator = 0
        skipNonAlphabetCharForwards = 0
        skipNonAlphabetCharBackwords = 0
        while iterator+skipNonAlphabetCharForwards <= len(s)-iterator-skipNonAlphabetCharBackwords - 1:
            if s[iterator+skipNonAlphabetCharForwards].isalnum() == True and s[len(s)-iterator-skipNonAlphabetCharBackwords - 1].isalnum() == True:
                if s[iterator+skipNonAlphabetCharForwards].lower() == s[len(s)-iterator-skipNonAlphabetCharBackwords - 1].lower():
                    iterator+=1
                else:
                    return False
            else:
                if s[iterator+skipNonAlphabetCharForwards].isalnum() == False:
                    skipNonAlphabetCharForwards+=1
                if s[len(s)-iterator-skipNonAlphabetCharBackwords - 1].isalnum() == False:
                    skipNonAlphabetCharBackwords+=1     
        return True
