class Solution:
    def singleNumber(self, nums):
        x = 0
        for num in nums:
            x ^= num
        return x

            

