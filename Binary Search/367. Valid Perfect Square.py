class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 0:
            return False

        low = 0
        high = num
        while low <= high:
            mid = (low + high) >> 1
            if mid * mid == num:
                return True
            elif mid * mid < num:
                low = mid + 1
            else:
                high = mid - 1
        return False
