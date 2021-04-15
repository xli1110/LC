class Solution:
    def maximalSquare(self, matrix: [[str]]) -> int:
        if not matrix or not matrix[0]:
            raise Exception("Empty Matrix")

        dp = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        side_length = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if int(matrix[i][j]) == 0:
                    dp[i][j] = 0
                    continue

                if i == 0 or j == 0:
                    dp[i][j] = int(matrix[i][j])
                else:
                    dp[i][j] = min(
                        dp[i - 1][j],
                        dp[i][j - 1],
                        dp[i - 1][j - 1]
                    ) + 1

                if dp[i][j] > side_length:
                    side_length = dp[i][j]
        return side_length * side_length


if __name__ == "__main__":
    mat = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]

    sol = Solution()
    print(sol.maximalSquare(mat))
