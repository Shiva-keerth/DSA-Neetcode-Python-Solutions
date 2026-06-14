class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        """
        Time: O(n) | Space: O(1)
        Keep track of lowest price seen so far.
        """
        res = 0
        lowest = prices[0]
        for price in prices:
            if price < lowest:
                lowest = price
            res = max(res, price - lowest)
        return res
