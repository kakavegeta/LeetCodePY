class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        res = []
        if num == 0:
            return [0]
        res.append(0)
        res.append(1)
        for i in range(2, num+1):
            res.append(res[i>>1]+(i&1))
        return res

    def countBits2(self, num):
        # What an amazing method!!!
        counts = [0]
        if num==0:
            return counts
        while len(counts)<num+1:
            counts+=[i+1 for i in counts[:num+1-len(counts)]]
            print(counts)
        return counts

sol = Solution()
print(sol.countBits2(50))

# new knowledge:
# 1. shift operators
# 2. binary transformation