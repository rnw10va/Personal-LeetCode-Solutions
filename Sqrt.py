# Problem Name: Sqrt(s)
# Problem Link: https://leetcode.com/problems/sqrtx/description/

#Original Method that was fast enough but super slow compared to attempt 2.
"""
class Solution:
    def mySqrt(self, x: int) -> int:
        i = 0
        sqrd = 0
        while sqrd <= x:
            i += 1
            sqrd = i * i
        if sqrd == x:
            return i
        else:
            return i - 1

"""

#Second attempt that was much faster and aproximately the same memory use.
class Solution:
    def mySqrt(self, x: int) -> int:
        #Binary Search Method
        if x == 0:
            return 0
        left = 1
        right = x
        
        while left <= right:
            #So that the mid variable isn't stored as a long and waste memory
            mid = left + (right - left) // 2 
            if mid == x // mid:
                return mid
            elif mid > x // mid:
                right = mid - 1
            else:
                left = mid + 1
        return right
