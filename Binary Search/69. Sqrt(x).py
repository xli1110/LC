class Solution:
    def mySqrt(self, x: int) -> int:
        """
        Note return high when low > high.
        Actually high = low - 1.

        Example x = 5
        1 - low = 0, high = 5, mid = 2, 4 < 5
        2 - low = 3, high = 5, mid = 4, 16 > 5
        3 - low = 3, high = 3, mid = 3, 9 > 5
        4 - low = 3, high = 2, return 2
        """
        if x < 0:
            raise Exception("Square Root of a Negative Number")

        low = 0
        high = x

        while low <= high:
            mid = (low + high) >> 1
            t = mid * mid
            if t == x:
                return mid
            elif t < x:
                low = mid + 1
            else:
                high = mid - 1
        return high  # note
