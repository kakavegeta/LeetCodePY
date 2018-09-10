class Solution:

    def longestPalindrome(self, s):
        if s=="":
             return ""
        if len(s)==1:
            return s
        min_start = 0
        max_len = 1
        length = len(s)
        i = 0
        while i < length: 
            if length - i <= max_len/2:
                break
            j, k = i,i
            while k<length-1 and s[k]==s[k+1]:
                k +=1
            i = k+1
            while k<length-1 and j>0 and s[j-1]==s[k+1]:
                j-=1
                k+=1
            new_len = k-j+1
            if new_len>max_len:
                max_len = new_len
                min_start = j
        print(min_start, max_len)
        return s[min_start: min_start+max_len]
    
sol = Solution()
res = sol.longestPalindrome('cbba')
print(res)
            