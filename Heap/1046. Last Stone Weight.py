import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones:
            raise Exception("Empty Array")

        h = [-x for x in stones]
        heapq.heapify(h)

        while len(h) > 1:
            x = -heapq.heappop(h)
            y = -heapq.heappop(h)
            if x != y:
                heapq.heappush(h, -abs(x - y))
        return 0 if not h else -h[0]
