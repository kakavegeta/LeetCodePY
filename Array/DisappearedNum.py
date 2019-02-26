class Solution:
    def findDisappearedNumbers(self, nums):
        for num in nums:
            nums[abs(num)-1] = -abs(nums[abs(num)-1])
        return [i+1 for i in range(len(nums)) if nums[i]>0]
