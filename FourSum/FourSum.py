class Solution:
    # this code needs further corrected
    def fourSum(self, nums, target):

        def findNsum(nums, target, N, _res, res):
            length = len(nums)
            if nums[0]*N > target or nums[-1]*N < target or length < N or N < 2:
                return
            if N == 2:
                left, right = 0, length-1
                if nums[left]==nums[right]:
                    return nums[left]
                while left < right:
                    if nums[left] + nums[right] == target:
                        res.append([nums[left], nums[right]]+_res)
                        left+=1
                        right-=1
                        while nums[left] == nums[left-1] and left<right:
                            left += 1                            
                        while nums[right] == nums[right+1] and right>left:
                            right -= 1                            

                    elif nums[left]+nums[right] < target:
                        while nums[left] == nums[left+1]:
                            left += 1
                        left += 1
                    else:
                        while nums[right] == nums[right-1]:
                            right -= 1
                        right -= 1
            else:
                for i in range(length-N+1):
                    if i==0 or (i>0 and nums[i] != nums[i-1]):
                        findNsum(nums[i+1:], target-nums[i], N-1, _res+[nums[i]], res)

        res = []
        if nums==[]:
            return 
        nums.sort()
        findNsum(nums, target, 4, [], res)
        return res
if __name__=="__main__":
    sol = Solution()
    nums =  [0,1,5,0,1,5,5,-4]
    ans = sol.fourSum(nums, 11)
    print(ans)
