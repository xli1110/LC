class Problem:
    """
    Given a string S of length N, the task is to find the smallest balanced substring in S.
    If no such substring is present, print -1.
    A string is balanced if every letter in the string appears in both uppercase and lowercase.
    For instance, “AabB” is a balanced string whereas “Ab” is not a balanced string.
    The string may only contains 26 English letters.

    Input: S = “azABaabba”
    Output: ABaab
    Explanation:
    Substring {S[2], …, S[6]} (0-based indexing) is the smallest substring which is balanced.

    Input: S = “Technocat”
    Output: -1

    I have no time to complete this problem in the OA, screwed.
    The merge part has some problems, but there is not time for modifications.
    """

    def find_balanced_string(self, s):
        if not s:
            raise Exception("Empty Array")

        """
        Record the Indices of Lower-Upper Pairs
        See 3. Longest Substring Without Repeating Characters - <DP>
        """
        capital = [None] * 26
        regular = [None] * 26
        for i, ch in enumerate(s):
            if ch.isupper():
                capital[ord(ch) - ord("A")] = i
            else:
                regular[ord(ch) - ord("a")] = i

        """
        Record and Merge Intervals
        interval = [start, end]
        See 56. Merge Intervals - <Others>
        """
        # record intervals
        intervals = []
        for i in range(26):
            if capital[i] is not None and regular[i] is not None:
                intervals.append(
                    [
                        min(capital[i], regular[i]),
                        max(capital[i], regular[i]),
                    ]
                )
        if not intervals:
            return -1

        # merge intervals
        intervals.sort(key=lambda x: x[0])  # note this sort
        # init
        merged_intervals = []
        start = intervals[0][0]
        end = intervals[0][1]
        # loop
        for i in range(1, len(intervals)):
            x = intervals[i]
            if x[0] > end:
                # [1, 5], [20, 30]
                merged_intervals.append([start, end])
                start = x[0]
                end = x[1]
            else:
                # [1, 5], [3, 6]
                # [1, 5], [3, 4] - Note this case, we need to consider which end is larger.
                end = max(end, x[1])
        # After we visit the last item in intervals, the last [start, end] pair will not be added to res.
        # We append the last pair manually.
        merged_intervals.append([start, end])

        """
        Find the Minimum Substring
        """
        min_length = len(s)  # init
        res = None

        for interval in merged_intervals:
            cur_length = interval[1] - interval[0] + 1
            if cur_length < min_length:
                min_length = cur_length
                res = interval

        return s[res[0]: res[1]]


if __name__ == "__main__":
    p = Problem()

    s = "azABaabba"
    print(p.find_balanced_string(s))
