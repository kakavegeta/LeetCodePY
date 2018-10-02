class Solution:
    def climbStairs(self, n):
        f0 = 0
        f1 = 1
        for _ in range(n):
           f1, f0 = f0+f1, f1
        return f1

sol = Solution()
print(sol.climbStairs(3))