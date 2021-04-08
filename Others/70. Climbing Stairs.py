class Solution:
    def climbStairs(self, n: int) -> int:
        """
        dp[i] = dp[i - 1] + dp[i - 2]
        Fibonacci Series
        """
        if n < 0:
            raise Exception("Negative Number of Stairs")

        if n == 1:
            return 1

        if n == 2:
            return 2

        x = 1
        y = 2
        for _ in range(n - 1):
            x, y = y, x + y
        return x
