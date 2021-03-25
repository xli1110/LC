# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):


class Solution:
    def firstBadVersion(self, n):
        """
        Notes:
        1 - Check corner cases.
            1.1 - Empty Input
            1.2 - No bad version.
            1.3 - All bad version.
        2 - Similar to 33, low designating to the end of good version, and high designating to the start of bad version.
        Since we assume low/high designates to good/bad, we must check corner cases 1.2 and 1.3.
        """
        if n < 1:
            raise Exception("There is no version.")

        if not isBadVersion(n):
            raise Exception("There is no bad version.")

        if isBadVersion(1):
            return 1

        low = 1
        high = n

        while high - low > 1:
            mid = (low + high) >> 1
            if isBadVersion(mid):
                high = mid
            else:
                low = mid

        return high
