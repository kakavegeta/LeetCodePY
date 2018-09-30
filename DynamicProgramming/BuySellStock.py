class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices==[]:
            return
        length = len(prices)
        profits = [0]*length
        for i in range(length):
            if i==0:
                profits[i]==0
            else:
                profits[i]=prices[i]-prices[i-1]
        max_ending_here, max_sofar = profits[0], profits[0]
        #prev indicates the i-1 position maxprofits
        #cur indicates the i position maxprofits
        for profit in profits:
            max_ending_here = max(profit, max_ending_here+profit)
            max_sofar = max(max_sofar, max_ending_here)
        return max_sofar
    
    def maxProfit2(self, prices):
        if not prices:
            return 0
        maxprofit = 0
        buycost = prices[0]
        for price in prices[1:]:
            if price<buycost:
                buycost = price
            if maxprofit<price-buycost:
                maxprofit = price-buycost
        return maxprofit

if __name__=='__main__':
    nums = [7,1,5,3,6,4]
    sol = Solution()

    print(sol.maxProfit2(nums))
