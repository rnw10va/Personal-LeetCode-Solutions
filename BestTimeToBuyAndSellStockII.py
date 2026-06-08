"""
Problem Name: 2. Problem Name: 122. Best Time to Buy and Sell Stock II
Problem Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/
Problem Description:
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.


Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]


Constraints:

    The number of nodes in each linked list is in the range [1, 100].
    0 <= Node.val <= 9
    It is guaranteed that the list represents a number that does not have leading zeros.
"""

#My Solution
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        currentSmallestBuyPrice = prices[0]
        for i in range(1,len(prices)):
            if currentSmallestBuyPrice < prices[i]:
                profit+=prices[i]-prices[i-1]
                currentSmallestBuyPrice = prices[i]
            else:
                currentSmallestBuyPrice = prices[i]
        return profit