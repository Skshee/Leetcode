'''
Link : https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
Can solve using either methods
'''

# Method 1 

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        
        for price in prices[1:]:
            if price < min_price:
                min_price = price  # Best price to buy so far
            else:
                max_profit = max(max_profit, price - min_price) 
        
        return max_profit
    

