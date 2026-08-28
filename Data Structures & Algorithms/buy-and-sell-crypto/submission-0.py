class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_price = prices[0]
        output = 0

        for price in prices:
            if price < lowest_price:
                lowest_price = price

            profit = price - lowest_price
            output = max(output, profit)
        return output




        