class Solution:

    def DFS(self, mat, word, i, j, k):
        """
        Do not forget to pop when going up.
        """
        if k == len(word):  # match complete
            return True
        if i >= len(mat) or j >= len(mat[0]) or i < 0 or j < 0:  # index exceeds
            return False
        if mat[i][j] != word[k]:  # check match
            return False

        temp = mat[i][j]
        mat[i][j] = None  # going down, avoid repetition
        res = self.DFS(mat, word, i + 1, j, k + 1) \
              or self.DFS(mat, word, i - 1, j, k + 1) \
              or self.DFS(mat, word, i, j + 1, k + 1) \
              or self.DFS(mat, word, i, j - 1, k + 1)
        mat[i][j] = temp  # going up, pop
        return res

    def exist(self, board: [[str]], word: str) -> bool:
        if not board or not board[0]:
            raise Exception("Empty Matrix")

        if not word:
            raise Exception("Empty Word")

        M = len(board)
        N = len(board[0])
        for i in range(M):
            for j in range(N):
                if self.DFS(board, word, i, j, 0):
                    return True
        return False


if __name__ == "__main__":
    sol = Solution()

    board = [["A", "B", "C", "E"], ["S", "F", "E", "S"], ["A", "D", "E", "E"]]
    word = "ABCESEEEFS"

    print(sol.exist(board, word))
