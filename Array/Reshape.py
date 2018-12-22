class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        m, n = len(nums), len(nums[0])
        if r*c != m*n or m==0:
            return nums
        res = [[0 for _ in range(c)] for _ in range(r)]
        count = 0
        for i in range(m):
            for j in range(n):
                res[count//c][count%c] = nums[i][j]
                count += 1
        return res

class Solution2:
    def matrixReshape(self, nums, r, c):
        flat = [j for i in nums for j in i]
        if len(flat)!=r*c or len(nums)==0:
            return nums
        res = []
        for i in range(r):
            res.append(flat[i*c: (i+1)*c])
        return res

sol = Solution2()
print(sol.matrixReshape([[1,2],
 [3,4]],1,4))


