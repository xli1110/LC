"""
3. Longest Substring Without Repeating Characters
    # init
    dic = {s[0]:0}
    dp = [1] * len(s)

    # loop
    for i in range(1, len(s)):
        if s[i] in dic:
            if i - dic[s[i]] <= dp[i - 1]:
                dp[i] = i - dic[s[i]]
            else:
                dp[i] = dp[i - 1] + 1
        else:
            dp[i] = dp[i - 1] + 1

        dic[s[i]] = i

53. Maximum Subarray
    # init
    dp = [arr[0]]

    # loop
    for i in range(1, len(arr)):
        if dp[i - 1] < 0:
            dp.append(arr[i])
        else:
            dp.append(dp[i - 1] + arr[i])

55. Jump Game
    # init
    i = 0
    right_most = 0

    # loop
    while i <= len(arr) - 1:
        if i > right_most:
            return False
        if i + arr[i] > right_most:
            right_most = i + arr[i]
        if right_most >= len(arr) - 1:
            return True
    return False

62. Unique Paths
    dp[i][j] = dp[i - 1] + dp[j - 1] if exist

64. Minimum Path Sum
    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j] if exist

70. Climbing Stairs
    dp[i] = dp[i - 1] + dp[i - 2]

96. Unique Binary Search Trees
    Suck

121. Best Time to Buy and Sell Stock
    # init
    low = arr[0]
    profit = 0

    # loop
    for i in range(1, len(arr)):
        if arr[i] - low > profit:
            profit = arr[i] - low
        if arr[i] < low:
            low = arr[i]

139. Word Break
    # init
    dp = [False] * len(s)

    # loop
    for i in range(len(s)):
        for j in range(i, len(s)):
            if i == 0:
                if s[:j + 1] in word_set:
                    dp[j] = True
            else:
                if dp[i - 1] and s[:j + 1] in word_set:
                    dp[j] = True

152. Maximum Product Subarray
    Suck

198. House Robber
    consider this example: arr = [100, 1, 1, 1, 100]

    dp[i] - the current max profit

    # init
    dp[0] = arr[0]
    dp[1] = max(arr[0], arr[1]), note it is not arr[1]

    # loop
    dp[i] = max(dp[i - 1], dp[i - 2] + x)

213. House Robber II
    dp_0 traverses arr[:-1]
    dp_1 traverse arr[1:]

    return max(max(dp_0), max(dp_1))

221. Maximal Square
    dp[i][j] - the maximal square's SIDE LENGTH whose bottom right corner is [i][j]

    if mat[i][j] != 0:
        dp[i][j] = min(
            dp[i - 1][j],
            dp[i][j - 1],
            dp[i - 1][j - 1]
        ) + 1

    Draw a picture with
    dp[i - 1][j] = 2
    dp[i][j - 1] = 3
    dp[i - 1][j - 1] = 3
    to understand the transfer function.

279. <TBD>Perfect Squares

300. Longest Increasing Subsequence
    dp[i] represents the longest sub-sequence ENDING AT arr[i]

    dp = [1] * len(arr)
    for i in range(arr):
        for j in range(i):
            if arr[j] < arr[i]:  # update condition
                temp_max = dp[j] + 1
                if temp_max > dp[i]:
                    dp[i] = temp_max

309. <TBD>Best Time to Buy and Sell Stock with Cooldown

322. <TBD>Coin Change

337. House Robber III
    x_0 = the maximal value if we do NOTvisit the current node
    x_1 = the maximal value if we visit the current node

    The relationship between L and R is PLUS.
    The relationship between children and parent is like 198.
    dp[i] = dp[i - 1] => node_0 = max(L0, L1) + max(R0, R1)
    dp[i] = dp[i - 2] + x => node_1 = L0 + R0 + node.val

338. <TBD>Counting Bits

416. <TBD>Partition Equal Subset Sum

494. <TBD>Target Sum
"""
