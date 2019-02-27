class Solution:
    def imageSmoother(self, M):
        r, c = len(M), len(M[0])
        ans = [[None for _ in range(c)] for _ in range(r)]
        dirs = [(0,1), (0,-1), (1,0),(-1,0),(-1,-1),(-1,1),(1,1), (1,-1)]
        for i in range(r):
            for j in range(c):
                val, cnt = M[i][j], 1
                for m, n in dirs:
                    x, y = i+m, j+n
                    if x<0 or x>r-1 or y<0 or y>c-1:
                        continue
                    val += M[x][y]
                    cnt += 1
                ans[i][j] = val//cnt
        return ans



