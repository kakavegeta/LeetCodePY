class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        return  [[A[i][j] for i in range(len(A))] for j in range(len(A[0]))]

sol = Solution()
print(sol.transpose([[1,2,3],[4,5,6],[7,8,9]]))