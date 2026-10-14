class Solution:
    def maxProfit(self, k: int, prices: list[int]) -> int:
        if not prices or k == 0:
            return 0
        
        n = len(prices)
        
        # If k is very large, the problem reduces to unlimited transactions (Stock II)
        if k >= n // 2:
            return sum(max(0, prices[i] - prices[i - 1]) for i in range(1, n))
        
        # dp[i][0] -> min cost/price to buy up to i-th transaction
        # dp[i][1] -> max profit after selling up to i-th transaction
        buy = [-prices[0]] * (k + 1)
        sell = [0] * (k + 1)
        
        for price in prices:
            for i in range(1, k + 1):
                buy[i] = max(buy[i], sell[i - 1] - price)
                sell[i] = max(sell[i], buy[i] + price)
                
        return sell[k]