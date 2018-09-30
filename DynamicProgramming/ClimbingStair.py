class Solution():
    def minCostClimbingStairs(self, costs):
        m1, m2 = 0, 0
        for cost in costs:
            m1, m2 = cost+min(m1,m2), m1
        return min(m1,m2)





