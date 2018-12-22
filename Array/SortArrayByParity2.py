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
                A[i], A[j] = A[j], A[i]
        return A

class Solution3:
    def sortArrayByParityII(self, A):
        i, j, n = 0, 1, len(A) 
        while i<n and j<n:
            while i<n and A[i]%2==0:
                i += 2
            while j<n and A[j]%2==1:
                j += 2
            if i<n and j<n:
                A[i], A[j] = A[j], A[i]
        return A
"""
just make sure A[0], A[2], A[4]... being even;
to do this, seperate A into two lists E and O, one by odd position, one by even position;
for each even i in E(from 0), if A[i] is even, pass it;
    if A[i] is odd, then pass j through O(from 1) until finding an even one, and swap A[i], A[j] 
"""                

sol = Solution3()
print(sol.sortArrayByParityII([4,2,5,7,9,12]))