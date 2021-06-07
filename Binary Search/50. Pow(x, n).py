class Solution:
    def recur(self, x, n):
        if n == 0:
            return 1

        t = self.recur(x, n >> 1)

        return t * t if n & 1 == 0 else t * t * x

    def myPow(self, x: float, n: int) -> float:
        """
        O(logN)
        O(logN) - call stack
        """
        if x == 0 and n < 0:
            """
            TBD
            How to check corner case (0)^(-4)?
            x == 0 may not work, in terms of the data type precision problem.
            """
            raise Exception("Invalid Input: {0}^{1}".format(x, n))

        return self.recur(x, n) if n >= 0 else 1 / self.recur(x, -n)  # passing NEGATIVE n when n < 0


if __name__ == "__main__":
    sol = Solution()
    print(sol.recur(2, -2))
