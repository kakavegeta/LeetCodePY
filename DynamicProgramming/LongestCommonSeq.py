def LSC_TD(x, y):
    memo = {}
    def dp_recur(x, y, i, j):
        if i<0 or j<0:
            return 0
        memo.setdefault((i,j),None)
        if memo[(i,j)] is None:
            if x[i] == y[j]:
                memo[(i,j)] = dp_recur(x, y, i-1, j-1)+1
            else:
                memo[(i,j)] = max(dp_recur(x,y,i,j-1), dp_recur(x,y,i-1,j))
        return memo[(i,j)]
    return dp_recur(x,y,len(x)-1,len(y)-1)


def LSC_BU(x,y):
    m, n = len(x), len(y)
    memo = [[0]*(n+1)]*(m+1)
    for i in range(m):
        for j in range(n):
            if x[i] == y[j]:
                memo[i+1][j+1] = memo[i][j]+1
            else:
                memo[i+1][j+1] = max(memo[i][j+1], memo[i+1][j])
    print(memo)
    return memo[m][n]

                
def LSC_BU2(x,y):
    '''space optimization'''
    m, n = len(x), len(y)
    memo = [[0]*(n+1)]*2
    for i in range(m):
        for j in range(n):
            if x[i]==y[j]:
                memo[1][j+1] = memo[0][j]+1
            else:
                memo[1][j+1] = max(memo[0][j+1], memo[1][j])
        print(memo)
        memo[0] = memo[1].copy()
    return memo[1][n]

def LSC_BU3(x,y):
    '''space optimization'''
    m, n = len(x), len(y)
    memo = [[0]*(n+1)]*2
    p = 0
    for i in range(m):
        p &= 1
        for j in range(n):
            if x[i]==y[j]:
                memo[p][j+1] = memo[1-p][j]+1
            else:
                memo[p][j+1] = max(memo[1-p][j+1], memo[p][j])
        print(memo)
    return memo[p][n]
            

                


if __name__ == "__main__":
    x = 'ABCBDAB'
    y = 'BDCABA'
    m = LSC_BU3(x,y)
    print(m)