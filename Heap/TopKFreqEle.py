import heapq
class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq = {}
        pq, res = [], []
        for c in nums:
            if c not in freq:
                freq[c] = 1
            else:
                freq[c] += 1
        for key, value in freq.items():
            heapq.heappush(pq,(-value, key))
        for _ in range(k):
            res.append(heapq.heappop(pq)[-1])
        return res 