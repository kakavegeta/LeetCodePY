class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)
        memo = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for j in range(n):
            memo[0][j+1] = memo[0][j] + ord(s2[j])
        for i in range(m):
            memo[i+1][0] = memo[i][0] + ord(s1[i])
        print(memo)
        for i in range(m):
            for j in range(n):
                    if s1[i]==s2[j]:
                        memo[i+1][j+1] = memo[i][j]
                    else:
                        memo[i+1][j+1] = min(memo[i][j+1]+ord(s1[i]),
                                        memo[i+1][j]+ord(s2[j]))
        return memo[m][n]
    
    def minimumDeleteSum2(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)
        memo = [0]*(n+1)
        for j in range(n):
            memo[j+1]= memo[j] + ord(s2[j])
        for i in range(m):
            ss1= memo[0]
            memo[0] += ord(s1[i])
            for j in range(n):
                ss2 = memo[j+1]
                if s1[i]==s2[j]:
                    memo[j+1] = ss1
                else:
                    memo[j+1] = min(memo[j+1]+ord(s1[i]),
                                    memo[j]+ord(s2[j]))
                ss1 = ss2
        return memo[n]
        
if __name__ == "__main__":
    sol = Solution()
    s1 = 'ab'
    s2 = 'ab'
    res = sol.minimumDeleteSum2(s1, s2)
    print(res)