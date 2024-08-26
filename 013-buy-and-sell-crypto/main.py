class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # Time Complexity: O(n)
        # Space Complexity: O(1)

        res = 0
        lowest = prices[0]

        for price in prices:
            if price < lowest:
                lowest = price
            res = max(res, price - lowest)
        return res
