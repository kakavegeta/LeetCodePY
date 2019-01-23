class Solution:
    def threeSumClosest(self, nums, target):
        '''
        :type nums: list[int]
        :type target: int
        :rtype: int
        '''
        n = len(nums)
        nums.sort()
        minv = 0
        for i in range(n-1):
            while nums[i] == nums[i+1]:
                i += 1
            lo = i + 1
            hi = n - 1
            _target = target-nums[i]
            resid = _target-nums[lo]-nums[hi]
