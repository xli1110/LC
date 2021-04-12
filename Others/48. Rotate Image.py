class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix or not matrix[0]:
            raise Exception("Empty Image")
        if len(matrix) != len(matrix[0]):
            raise Exception("Non-Square Image")

        n = len(matrix)
