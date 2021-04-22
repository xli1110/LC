class Solution:
    def expand(self, s, low, high):
        num = 0
        while low >= 0 and high <= len(s) - 1:
            if s[low] == s[high]:
                num += 1
                low -= 1
                high += 1
            else:
                break
        return num

    def countSubstrings(self, s: str) -> int:
        num = 0
        for i in range(len(s)):
            num += self.expand(s, i, i)

            if i < len(s) - 1:
                num += self.expand(s, i, i + 1)
        return num
