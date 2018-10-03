class Solution:
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        dp = 0
        num = 0
        for i in range(2, len(A)):
            if A[i]+A[i-2]==2*A[i-1]:
                dp+=1
                num+=dp
            else:
                dp=0
        return num

sol = Solution()
print(sol.numberOfArithmeticSlices([1, 2, 3, 4]))
