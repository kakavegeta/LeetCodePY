class Solution:
    def sumEvenAfterQueries(self, A: 'List[int]', queries: 'List[List[int]]') -> 'List[int]':
        Sum, res = 0, []
        for a in A:
            if not a&1: Sum += a
        for q in queries:
            i = q[1]
            if not A[i]&1: Sum -= A[i]
            A[i] += q[0]
            if not A[i]&1: Sum += A[i]
            res.append(Sum)
        return res
            
        
        