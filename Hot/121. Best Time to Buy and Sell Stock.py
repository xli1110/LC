class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            raise Exception("No Available Prices")

        low = prices[0]  # lowest HISTORICAL price
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] - low > profit:
                profit = prices[i] - low
            if prices[i] < low:
                low = prices[i]
        return profit
