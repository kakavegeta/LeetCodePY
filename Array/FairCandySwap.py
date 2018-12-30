class Solution:
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        suma, sumb = sum(A), sum(B)
        diff = (sumb - suma)//2
        A = set(A)
        B = set(B)
        for a in A:
            if a + diff in B:
                return [a, a+diff]
     