class Solution:
    def expand(self, s, low, high):
        """
        Two break cases returning the same result, so there is no need to distinguish them.

        break 1: digit difference
        s = xabaxx, center = 2, low = 0, high = 4
        return s[low + 1:high]

        break 2: index exceeds
        s = abaxx, center = 1, low = -1, high = 3
        s = xxaba, center = 3, low = 1, high = 5
        return s[low + 1:high]
        """
        while low >= 0 and high <= len(s) - 1:
            if s[low] != s[high]:
                break
            else:
                low -= 1
                high += 1
        return low, high

    def longestPalindrome(self, s: str) -> str:
        if not s:
            raise Exception("Empty String")

        res_low = 0
        res_high = 0
        for i in range(len(s)):
            # center = i
            low, high = self.expand(s, i, i)
            if high - low > res_high - res_low:
                res_high, res_low = high, low

            # center between i and (i + 1)
            if i != len(s) - 1:
                low, high = self.expand(s, i, i + 1)
                if high - low > res_high - res_low:
                    res_high, res_low = high, low

        return s[res_low + 1:res_high]
