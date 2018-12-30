class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        length = len(nums)
        for i in range(length):
            val = abs(nums[i])-1
            if nums[val]>0:
                nums[val] = -nums[val]
        for i in range(length):
            if nums[i]>0:
                res.append(i+1)
        return res

sol = Solution()
print(sol.findDisappearedNumbers([4,3,2,7,8,2,3,1]))
