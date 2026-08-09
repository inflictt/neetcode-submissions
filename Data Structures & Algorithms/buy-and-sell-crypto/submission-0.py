class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        n = len(prices)
        # brute idea of 2 loops
        for i in range(0, n):
            buy = prices[i]
            for j in range(i + 1, n):
                curr = prices[j]
                if buy < curr:  # ideal profit case 7 < 8
                    maxProfit = max(maxProfit, curr - buy)
                elif buy >= curr:  # eitheer got 7 == 7 or 7>1 dont sell
                    continue
        return maxProfit
