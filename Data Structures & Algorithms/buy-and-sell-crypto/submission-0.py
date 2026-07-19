class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit: int = 0
        for i, buy in enumerate(prices):
            for sell in prices[i + 1:]:
                if (sell - buy) > profit:
                    profit = sell - buy
        return profit