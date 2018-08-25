class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if len(s) < numRows:
            return s
        if numRows==1:
            return s
        res = ['' for _ in range(numRows)]
        currow = 0
        godown = 0
        for _s in s:
            res[currow] += _s
            if currow==0 or currow==numRows-1:
                godown ^= 1 
            if godown:
                currow+=1
            else:
                currow-=1
        return ''.join(res)

        


sol = Solution()
ans = sol.convert('ABCDEFG',3)
print(ans)