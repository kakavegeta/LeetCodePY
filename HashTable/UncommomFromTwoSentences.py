import collections
class Solution:
    def uncommonFromSentences(self, A: 'str', B: 'str') -> 'List[str]':
        alist = A.split()
        blist = B.split()
        c = collections.Counter(alist+blist)
        ret = []
        for word, num in c.items():
            if num==1:
                ret.append(word)
        return ret
        