class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """
        Since all elements are non-negative, we should never move to left or top.
        These movements increase the path length and also the path value.
        """
        if not grid or not grid[0]:
            raise Exception("Empty Grid")

        dp = [[0] * len(grid[0]) for _ in range(len(grid))]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j == 0:
                    dp[i][j] = grid[i][j]
                elif i == 0 and j != 0:
                    dp[i][j] = dp[i][j - 1] + grid[i][j]
                elif i != 0 and j == 0:
                    dp[i][j] = dp[i - 1][j] + grid[i][j]
                else:
                    dp[i][j] = min(dp[i][j - 1], dp[i - 1][j]) + grid[i][j]

        return dp[-1][-1]
