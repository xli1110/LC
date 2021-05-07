"""
Tips:
    1 - Library heapq, note that heapify has no return value, and it is a minimum-root heap.

        import heapq
        h = arr
        heapq.heapify(h) - O(N), note this linear complexity
        heapq.heappush(h, val) - O(logN)
        x = heapq.heappop(h) - O(logN)

    2 - For maximum-root heap, use opposite number.
        h = [-x for x in arr]
        heapq.heapify(h)



1 - Kth in Stream
    Kth largest => minimum-root heap
    Kth smallest => maximum-root heap

    Problems:
    703(Kth largest in a stream)
    1046/Amazon Fulfillment Builder - heap + combination rule
    Offer - 41(median in stream) - two heaps
"""
