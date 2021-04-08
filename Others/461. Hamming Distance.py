class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        if x < 0 or y < 0:
            raise Exception("Negative Input(s)")

        h_dist = 0
        while x > 0 or y > 0:
            if (x ^ y) & 1 == 1:
                h_dist += 1
            x >>= 1
            y >>= 1
        return h_dist
