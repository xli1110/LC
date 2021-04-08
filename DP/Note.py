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

53. Maximum Subarray - <DP>
    # init
    dp = [arr[0]]

    # loop
    for i in range(1, len(arr)):
        if dp[i - 1] < 0:
            dp.append(arr[i])
        else:
            dp.append(dp[i - 1] + arr[i])

70. Climbing Stairs - <Recursion, DP>
    dp[i] = dp[i - 1] + dp[i - 2]

121. Best Time to Buy and Sell Stock - <DP>
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