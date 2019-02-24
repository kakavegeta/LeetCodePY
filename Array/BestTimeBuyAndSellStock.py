class Solution:
    def maxProfit(self, prices):
        max_cur, max_sofar = 0, 0
        for i in range(len(prices)):
            max_cur += prices[i]-prices[i-1]
            max_cur = max(0, max_cur)
            max_sofar = max(max_cur, max_sofar)
        return max_sofar