class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        n, m = len(matrix[0]), len(matrix)
        for i in range(m):
            for j in range(n):    
                if i>0 and j>0 and matrix[i][j]!=matrix[i-1][j-1]:
                    return False
        return True

sol = Solution()
print(sol.isToeplitzMatrix([
  [1,2],
]))