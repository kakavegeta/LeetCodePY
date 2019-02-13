class Solution:
    def islandPerimeter(self, grid: 'List[List[int]]') -> 'int':
        land, neighbor = 0, 0 
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]==1:
                    land+=1
                    if i+1<len(grid) and grid[i+1][j]==1: #down neighbor
                        neighbor+=1
                    if j+1<len(grid[i]) and grid[i][j+1]==1: #down neighbor
                        neighbor+=1
        return land*4 - neighbor*2
    

    def islandPerimeter2(self, grid):
        #iterative
        m, n = len(grid), len(grid[0])
        if m==0:
            return 0
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    if i==0 or grid[i-1][j]==0:
                        ans+=1
                    if i==m-1 or grid[i+1][j]==0:
                        ans+=1
                    if j==0 or grid[i][j-1]==0:
                        ans+=1
                    if j==n-1 or grid[i][j+1]==0:
                        ans+=1
        return ans