class Solution:
    def fourSum(self, nums, target):
        nums.sort()

        def findNsum(nums, target, N, _res, res):
            nums.sort()
            res = []
            length = len(nums)
            if nums[0]*N > target or nums[-1]*N < target or length < N or N < 2:
                return
            if N == 2:
                left, right = 0, length-1
                while left < right:
                    if nums[left] + nums[right] == target:
                        res.append([nums[left], nums[right]]+_res)
                        while nums[left] == nums[left+1]:
                            left += 1
                        while nums[right] == nums[right-1]:
                            right -= 1
                        left += 1
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
                    if nums[i] != nums[i+1]:
                        findNsum(nums[i+1:], target-nums[i], N-1, _res+[nums[i]], res)

        res = []
        findNsum(nums, target, 4, [], res)
        return res
if __name__=="__main__":
    sol = Solution()
    nums = [1, 0, -1, 0, -2, 2]
    ans = sol.fourSum(nums, 0)
    print(ans)
