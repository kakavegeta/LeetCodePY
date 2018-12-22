class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        res = 0
        for i in range(len(nums)):
            if not i %2:
                res += nums[i]
        return res

sol = Solution()
print(sol.arrayPairSum([1,4,3,2]))