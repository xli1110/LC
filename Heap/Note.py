"""
Tips:
    - heapq library, note that heapify has no return, it is a minimum-root heap
        import heapq
        h = arr
        heapq.heapify(h) - O(N), note this linear complexity
        heapq.heappush(h, val) - O(logN)
        x = heapq.heappop(h) - O(logN)
    - for maximum-root heap, use opposite number
        h = [-x for x in arr]
        heapq.heapify(h)

1 - Stream
    kth largest, minimum-root heap(built-in); kth smallest, maximum-root heap

    Problems:
    703(kth largest in a stream)
    41Offer(median in stream) - two heaps

2 - Others
    215(kth largest in an array, comprehensive methods) - quick sort; heap; QUICK SELECT
    1046
"""