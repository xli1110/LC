class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if not board or not board[0]:
            raise Exception("Empty Board")
        if len(board) != 9 or len(board[0]) != 9:
            raise Exception("Invalid Board")

        # check each row
        for i in range(len(board)):
            s = set()
            for j in range(len(board[0])):
                x = board[i][j]
                if x != ".":
                    if x in s:
                        return False
                    else:
                        s.add(x)

        # check each column
        for j in range(len(board[0])):
            s = set()
            for i in range(len(board)):
                x = board[i][j]
                if x != ".":
                    if x in s:
                        return False
                    else:
                        s.add(x)

        # check square
        for row in range(3):
            for col in range(3):
                s = set()
                for i in range(row * 3, (row + 1) * 3):
                    for j in range(col * 3, (col + 1) * 3):
                        x = board[i][j]
                        if x != ".":
                            if x in s:
                                return False
                            else:
                                s.add(x)

        return True
