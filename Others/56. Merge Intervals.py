class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            raise Exception("Empty Array")

        res = []
        intervals.sort(key=lambda x: x[0])  # note this sort

        # init
        start = intervals[0][0]
        end = intervals[0][1]

        # loop
        for i in range(1, len(intervals)):
            x = intervals[i]

            if x[0] > end:
                # [1, 5], [20, 30]
                res.append([start, end])
                start = x[0]
                end = x[1]
            else:
                # [1, 5], [3, 6]
                # [1, 5], [3, 4] - Note this case, we need to consider which end is larger.
                end = max(end, x[1])

        # After we visit the last item in intervals, the last [start, end] pair will not be added to res.
        # We append the last pair manually.
        res.append([start, end])

        return res
