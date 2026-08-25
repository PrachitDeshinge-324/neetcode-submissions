class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell, profit = 0,1,0
        for i in range(1,len(prices)):
            if prices[i] < prices[buy]:
                buy = i
            elif (prices[i]-prices[buy])>profit:
                sell = i
                profit = prices[sell] - prices[buy]
        return profit