from functools import reduce
class Solution:
    def letterCombinations(self, digits):
        if digits=="":
            return []
        charmap = ['0','1','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
        return reduce(lambda accm, digit:[i+j for i in accm for j in charmap[int(digit)]], digits, [''])
sol = Solution()
ans = sol.letterCombinations('23')
print(ans)