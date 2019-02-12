import random
class Solution:
    def repeatedNTimes(self, A):
        res = {}
        for e in A:
            if e in res:
                res[e]+=1
                if res[e]>1:
                    return res[e]
            else:
                res[e] = 0
    
    def repeatedNtimes2(self, A):
        i, j, n = 0, 0, len(A)
        while i==j or A[i]!=A[j]:
            i = random.randrange(0, n)
            j = random.randrange(0, n)
        return A[i]

        
        