class Solution:
    def digit_square(self, n):
        res = 0
        while n > 0:
            res += (n % 10) * (n % 10)
            n //= 10
        return res

    def isHappy(self, n: int) -> bool:
        if n < 0:
            raise Exception("Invalid Input")
        s = set()
        while n != 1:
            if n in s:
                return False
            s.add(n)
            n = self.digit_square(n)

        return True
