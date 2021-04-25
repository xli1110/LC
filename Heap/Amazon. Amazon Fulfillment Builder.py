import heapq


class Problem:
    """
    Amazon Fulfillment Builder
    Similar to leetcode 1046.

    Assemble the two lightest goods and put the combination into the array,
    until there are less than two goods.
    """

    def combineParts(self, parts):
        """
        O(NlogN)
        """
        # Write your code here
        heapq.heapify(parts)

        time = 0

        while len(parts) > 1:
            x1 = heapq.heappop(parts)
            x2 = heapq.heappop(parts)
            t = x1 + x2

            time += t
            heapq.heappush(parts, t)

        return time
