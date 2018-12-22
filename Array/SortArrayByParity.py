class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: list[int]
        :rtype: list[int]
        """
        res1 = []
        res2 = []
        for i in A:
            if i%2 == 0:
                res1.append(i)
            else:
                res2.append(i)
        return res1 + res2

class Solution2:
    def sortArrayByParity(self, A):
        A.sort(key=lambda x: x%2 != 0)
        return A

input = [3,1,2,4]
sol = Solution2()
print(sol.sortArrayByParity(input))