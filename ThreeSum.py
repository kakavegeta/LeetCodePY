class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        nums.sort()
        res = []
        for i in range(n-1):
            if i==0 or (i>0 and nums[i]!=nums[i-1]):
                lo = i+1
                hi = n-1
                target = -nums[i]
                while(lo<hi):
                    if nums[lo]+nums[hi]==target:
                        res.append([nums[i], nums[lo], nums[hi]])
                        while (lo<hi and nums[lo]==nums[lo+1]):
                            lo+=1
                        while (lo<hi and nums[hi]==nums[hi-1]):
                            hi-=1
                        lo+=1
                        hi-=1
                    elif nums[lo]+nums[hi]<target:
                        lo+=1
                    else:
                        hi-=1
        return res

if __name__=='__main__':
    nums = [-1,0,1,2,-1,-4]
    sol = Solution()
    res = sol.threeSum(nums)
    print(res)
