class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            raise Exception("Empty Matrix")

        M = len(matrix)
        N = len(matrix[0])

        # search from the top right corner
        i = 0
        j = N - 1
        while 0 <= i <= M - 1 and 0 <= j <= N - 1:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                i += 1
            else:
                j -= 1
        return False
