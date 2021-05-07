class Solution:
    def numDecodings(self, s: str) -> int:
        """
        Similar to 70.
        Transfer from dp[i - 1] or dp[i - 2].

        Notes:
             1 - Transfer if char != "0".
             2 - Transfer from dp[i - 2] if int(s[i - 1:i + 1]) <= 26.
        """
        if not s:
            raise Exception("Empty Array")

        if len(s) == 1:
            return 1 if s[0] != "0" else 0

        # init
        dp = [0] * len(s)
        # dp[0]
        if s[0] != "0":
            dp[0] += 1
        # dp[1]
        if s[1] != "0":
            dp[1] += dp[0]
        if s[0] != "0" and int(s[0:2]) <= 26:
            dp[1] += 1

        # loop
        for i in range(2, len(s)):
            # transfer from dp[i - 1]
            if s[i] != "0":
                dp[i] += dp[i - 1]
            # transfer from dp[i - 2]
            if s[i - 1] != "0" and int(s[i - 1:i + 1]) <= 26:
                dp[i] += dp[i - 2]

        return dp[-1]
