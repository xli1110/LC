"""
Tips:
    - heapq library, note that heapify has no return, it is a minimum-root heap
        import heapq
        h = arr
        heapq.heapify(h)
        heapq.heappush(h, val)
        x = heapq.heappop(h)
    - for maximum-root heap, use opposite number
        h = [-x for x in arr]
        heapq.heapify(h)

1 - Stream
    kth largest, minimum-root heap(built-in); kth smallest, maximum-root heap

    Problems:
    703(kth largest in stream)
    41Offer(median in stream) - two heaps

2 - Others
    1046
"""
