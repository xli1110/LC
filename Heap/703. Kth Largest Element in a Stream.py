import heapq


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.h = nums
        heapq.heapify(self.h)

    def add(self, val: int) -> int:
        heapq.heappush(self.h, val)
        while len(self.h) > self.k:
            heapq.heappop(self.h)

        return None if len(self.h) < self.k else self.h[0]  # note there may be less than k elements in the heap

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
