import heapq


class Solution:
    def topKFrequent(self, nums: [int], k: int) -> [int]:
        """
        3 Traversals

        1 - Generate the dictionary.
        2 - Find the k largest frequencies.
            2.1 - heap with length k
            2.2 - quick select, see 215
        3 - Search elements whose freq >= heap[0].

        Note that 2 and 1 can NOT be done in one traversal, since d[x] may vary while looping.
        """
        if k <= 0:
            raise Exception("Invalid k {0}".format(k))

        d = {}
        for x in nums:
            if x in d:
                d[x] += 1
            else:
                d[x] = 1

        freq = []
        for x in d:
            if len(freq) < k:
                heapq.heappush(freq, d[x])
            else:
                heapq.heappush(freq, d[x])
                heapq.heappop(freq)

        res = []
        for x in d:
            if d[x] >= freq[0]:
                res.append(x)

        return res


if __name__ == "__main__":
    arr = [5, 3, 1, 1, 1, 3, 73, 1]
    k = 2

    sol = Solution()
    print(sol.topKFrequent(arr, k))
