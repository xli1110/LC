class Solution:
    def check(self, x):
        num = 0
        while x > 0:
            if x & 1 == 1:
                num += 1
            x >>= 1
        return num

    def brute_force(self, num):
        """
        O(32 * N)
        """
        res = []
        for x in range(num + 1):
            res.append(self.check(x))
        return res

    def countBits(self, num: int) -> List[int]:
        if num < 0:
            raise Exception("Negative Input")

        return self.brute_force(num)
