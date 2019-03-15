def LSC(x, y):
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


if __name__ == "__main__":
    x = 'ABCBDAB'
    y = 'BDCABA'
    m = LSC(x,y)
    print(m)