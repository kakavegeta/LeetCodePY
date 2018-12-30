class Solution:
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        ouside-in
        """
        A = []
        N = len(S)
        lo, hi = 0, N
        for s in S:
            if s=='D':
                A.append(hi)
                hi -= 1
            else:
                A.append(lo)
                lo += 1
        A.append(lo)
        return A
