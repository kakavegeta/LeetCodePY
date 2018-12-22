class Solution:
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        res1 = []
        res2 = []
        res = [0]*len(A)
        for i in A:
            if i%2 == 0:
                res1.append(i)
            else:
                res2.append(i)
        p = 0
        for i in res1:
            res[p] = i
            p += 2
        p = 1
        for i in res2:
            res[p] = i
            p += 2
        return res

class Solution2:
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        j = 1
        for i in range(0, len(A), 2):
            if A[i]%2:
                while A[j]%2:
                    j += 2
        return A
                
        

sol = Solution2()
print(sol.sortArrayByParityII([4,2,5,7]))