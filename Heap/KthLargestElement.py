import heapq
class KthLargest:

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self._queue = nums
        heapq.heapify(self._queue)
        self._k = k
        while len(self._queue) > k:
            heapq.heappop(self._queue)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if len(self._queue) < self._k:
            heapq.heappush(self._queue, val)
        else:
            heapq.heappushpop(self._queue, val)
        return self._queue[0]

if __name__ == "__main__":
    nums = [4,5,8,2]
    item = KthLargest(3, nums)
    print(item.add(3))
    print(item.add(4))
    print(item.add(5))