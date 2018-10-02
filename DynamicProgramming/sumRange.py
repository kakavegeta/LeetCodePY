class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        culsum = 0
        self.cache = [0]
        for num in nums:
            culsum+=num
            self.cache.append(culsum)
        print(self.cache)

        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.cache[j+1] - self.cache[i]

sol = NumArray([-2, 0, 3, -5, 2, -1])
print(sol.sumRange(0,5))
        