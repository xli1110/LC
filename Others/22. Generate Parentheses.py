class Solution:
    def __init__(self):
        self.res = []
        self.path = []

    def DFS(self, n, num_left, num_right):
        if num_left + num_right == 2 * n:
            self.res.append("".join(self.path))
            return

        if num_left < n:
            self.path.append("(")
            self.DFS(n, num_left + 1, num_right)
            self.path.pop()

        if num_right < num_left:  # note the condition: r < l
            self.path.append(")")
            self.DFS(n, num_left, num_right + 1)
            self.path.pop()

    def generateParenthesis(self, n: int) -> [str]:
        if n < 0:
            raise Exception("Negative n")

        self.DFS(n, 0, 0)
        return self.res


if __name__ == "__main__":
    sol = Solution()
    print(sol.generateParenthesis(1))
