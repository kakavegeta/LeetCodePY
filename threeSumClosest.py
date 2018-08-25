class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        nums.sort()
        ans = nums[0] + nums[1] + nums[2]
        if ans == target:
            return ans

        for i in range(n-2):
            lo = i+1
            hi = n-1
            while lo < hi:
                _sum = nums[lo] + nums[hi] + nums[i]
                if _sum==target:
                    return _sum

                if abs(target-ans)> abs(target-_sum):
                    ans = _sum
                
                if _sum > target:
                    hi-=1
                else:
                    lo+=1
        return ans

if __name__=='__main__':    
    sol = Solution()
    ans = sol.threeSumClosest([-1, 2, 1, -4], 0)
    print(ans)