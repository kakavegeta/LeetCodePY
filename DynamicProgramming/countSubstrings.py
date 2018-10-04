class Solution:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        count = 0
        for center in range(length):
            left =  right = center
            while left>=0 and right<=length-1 and s[left]==s[right]:
                count+=1
                left-=1
                right+=1
        for center in range(length):
            left = center
            right = center+1
            while left>=0 and right<=length-1 and s[left]==s[right]:
                count+=1
                left-=1
                right+=1
        return count
    def Manacher(self, s):
        string = self.preProcess(s)
        length = len(string)
        C = R = 0
        P = [0]*length
        for i in range(1,length-1):
            if R>i:
                P[i] = min(P[2*C-i], R-i)
            while string[i-P[i]-1]==string[i+P[i]+1]:
                P[i] += 1
            if R-i < P[i]:
                R = i + P[i]
                C = i
        return P
        

    def preProcess(self, s):
        return '@#'+'#'.join(s)+'#$'

sol = Solution()
print(sol.Manacher('aaa'))

