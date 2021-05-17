def max_sub_seq(arr):
    """
    Problem1
    Maximal Uncontinuous Sequence

    arr = [1, 2, 3, 4]
    res = 6 (2 + 4)

    arr = [-1, 1]
    res = 1

    arr = [-1, -1, -1, ...]
    res = 0

    length = 10 ^ 6



    dp[i] = max(dp[i - 1], dp[i - 2] + arr[i])

    dp[i - 1] = max(dp[i - 2], dp[i - 3] + arr[i - 1])
    """
    if not arr:
        raise Exception("Empty")
    if len(arr) == 1:
        return max(arr[0], 0)
    if len(arr) == 2:
        return max(arr[0], arr[1], 0)

    dp = [None] * len(arr)
    dp[0] = max(arr[0], 0)
    dp[1] = max(arr[0], arr[1], 0)

    for i in range(2, len(arr)):
        dp[i] = max(dp[i - 1], dp[i - 2] + arr[i])

    return max(max(dp), 0)


def max_sub_seq_2D(arr):
    """
    Problem2
    2D Case

    arr =
    [
    [1,2,3]
    [1,2,3]
    [1,2,3]
    ]

    res = 10 = 1, 3, 2, 1, 3

    arr <= 10 * 10



    1 - Try to find the dp transfer formulation -> Failed
    2 - Try brute-force search and discuss with the interviewer -> O(2 ^ 100)
    3 - Interviewer emphasized O(10 * 2 ^ 10), and discus this method.


    dp[i][j] =
    i: 0 -> cur row
    j: 101 -> previous state
    """
