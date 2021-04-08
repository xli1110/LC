import heapq


class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.h_great = []  # store x > median
        self.h_less = []  # store x < median

    def addNum(self, num: int) -> None:
        """
        1 - Note the NEGATIVE when operating elements from h_less.
        2 - Avoid compare num and heap root, because this will be too complex.
            Instead, repeatedly invoke push and pop, implementing the heap order property.
        """
        if len(self.h_great) != len(self.h_less):  # add an element to h_less
            heapq.heappush(self.h_great, num)
            heapq.heappush(self.h_less, -heapq.heappop(self.h_great))
        else:  # add an element to h_great
            heapq.heappush(self.h_less, -num)
            heapq.heappush(self.h_great, -heapq.heappop(self.h_less))

    def findMedian(self) -> float:
        if not self.h_great:  # no data in the stream
            return None
        return self.h_great[0] if len(self.h_great) != len(self.h_less) else (self.h_great[0] - self.h_less[0]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
