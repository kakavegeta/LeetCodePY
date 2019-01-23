class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        lo = 0
        hi = len(height)-1
        maxarea = 0
        while lo<hi:
            maxarea = max(maxarea, min(height[lo], height[hi])*(hi-lo))
            if height[lo]<height[hi]:
                lo+=1
            else:
                hi-=1
        return maxarea

sol = Solution()
area = sol.maxArea([1,8,6,2,5,4,8,3,7])
print(area)
