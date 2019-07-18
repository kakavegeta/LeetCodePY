class Solution:
    def minFallingPathSum(self, A):
        size = len(A)
        for i in range(1,size):
            for j in range(size):
                A[i][j] += min(A[i-1][max(0,j-1)], A[i-1][j], A[i-1][max(size-1,j+1)])
        return max(A[size-1])