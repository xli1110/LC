class Solution:
    def rotate(self, matrix: [[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.

        Example, side_length = 4

        A1 B1 C1 A2
        C4       B2
        B4       C2
        A4 C3 B3 A3

        1 - Divide the matrix into nested circles with side_length.
        2 - For each circle, swap X1-X2-X3-X4.

        i = (n - side_length) >> 1  # the current index of row

        j in range(i, n - i - 1)  # the current index of column

        X1 = [i][j]
        X2 = [j][n - 1 - i]
        X3 = [n - 1 - i][n - 1 - j]
        X4 = [n - 1 - j][i]
        """
        if not matrix or not matrix[0]:
            raise Exception("Empty Image")
        if len(matrix) != len(matrix[0]):
            raise Exception("Non-Square Image")

        n = len(matrix)
        side_length = n
        while side_length > 1:
            i = (n - side_length) >> 1
            # visit each column
            for j in range(i, n - i - 1):
                matrix[i][j], \
                matrix[j][n - 1 - i], \
                matrix[n - 1 - i][n - 1 - j], \
                matrix[n - 1 - j][i] \
                = \
                matrix[n - 1 - j][i], \
                matrix[i][j], \
                matrix[j][n - 1 - i], \
                matrix[n - 1 - i][n - 1 - j]

            side_length -= 2


if __name__ == "__main__":
    sol = Solution()

    # mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    mat = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]

    for row in mat:
        print(row)

    print("\n")

    sol.rotate(mat)
    for row in mat:
        print(row)
