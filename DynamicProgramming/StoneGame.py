class Solution:
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        n = len(piles)
        dp = [[0]*n for _ in range(n)]
        for i in range(n):
            dp[i][i] = piles[i]
        for j in range(1,n):
            for i in range(n-j):
                print(i,i+j)
                dp[i][i+j] = max(piles[i]-dp[i+1][i+j], piles[i+j]-dp[i][i+j-1])
        return dp[0][n-1]>0

    def stoneGame2(self, piles):
        n = len(piles)
        dp = piles.copy()
        for j in range(1,n):
            for i in range(n-j):
                dp[i] = max(p[i]-dp[i+1], p[i+j]-dp[i])
        return dp[0]>0




sol = Solution()
print(sol.stoneGame([5,3,4,5]))