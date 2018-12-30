class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        r = {}
        for num in nums:
            if num not in r:
                r[num] = 1
            else:
                r[num] += 1
        