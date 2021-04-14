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
"""
