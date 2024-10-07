# Problem Name: 122. Best Time to Buy and Sell Stock II
# Problem Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/

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
                
