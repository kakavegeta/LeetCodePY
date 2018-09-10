class Solution:
#the code is right, but when submit to leetcode, the last excuted input which is 'aaaaa....'
#will occur time limit exceed error
    def longestPalindrome(self, s):
        # define a boolean matrix record isPalindrom of substrings
        length = len(s)
        res = None
        if length<2:
            return s
        if s=="":
            return ""
        bmtx = [[0 for _ in range(length)] for _ in range(length)]
        i = length-1
        while i>=0:
            j = i
            while j<length:
                bmtx[i][j] = s[i]==s[j] and (j-i<3 or bmtx[i+1][j-1])
               
                if bmtx[i][j] and (res == None or len(res)<j-i+1):
                    res = s[i:j+1]
                j+=1
            i-=1
        return res
        
sol = Solution()
res = sol.longestPalindrome('abbc')
print(res)
        


