# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:


class Solution:
    def guessNumber(self, n: int) -> int:
        if n < 1:
            raise Exception("Invalid Input")

        low = 1
        high = n

        while low <= high:
            mid = (low + high) >> 1
            t = guess(mid)

            if t == 0:
                return mid
            elif t < 0:
                high = mid - 1
            else:
                low = mid + 1
        return -1
