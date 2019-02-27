import collections
class Solution:
    def findShortestSubArray(self, nums):
        begin, count = {},{}
        degree, ans = 0, 0
        for i, v in enumerate(nums):
            begin.setdefault(v, i)
            count[v] = count.get(v, 0) + 1
            if count[v]>degree:
                degree = count[v]
                ans = i - begin[v] + 1
            elif count[v] == degree:
                ans = min(ans, i-begin[v]+1)
        return ans
