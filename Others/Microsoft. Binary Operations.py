class Problem:
    """
    Given a string s representing a non-negative number num in the binary form.
    While num is not equal to 0, we have two operations as below.
    Operation1: If num is odd, we subtract 1 from it. 1101 -> 1100
    Operation2: If num is even, we divide 2 into it. 1100 -> 110

    The string s may contain leading zeroes.

    Calculate the number of operations we should take that transfers num to 0.

    Naive Method - (OA Result: Time Exceeds Limitation)
    O(N)
    O(1)
    """

    def find_start(self, s):
        """
        Remove leading zeroes.
        """
        start = 0
        while start < len(s):
            ch = s[start]
            if ch == "1":
                break
            elif ch == "0":
                start += 1
            else:
                raise Exception("Invalid Character {0}".format(ch))
        return start

    def string_num_transform(self, s):
        """
        Transform a string into a number.

        Built-In Function: num = int(s, 2)
        """
        power = 0
        num = 0

        start = self.find_start(s)
        end = len(s) - 1

        while end >= start:
            ch = s[end]
            if ch == "1" or ch == "0":
                num += int(ch) * (2 ** power)
                power += 1
                end -= 1
            else:
                raise Exception("Invalid Character {0}".format(ch))
        return num

    def calculate_num_operations(self, s):
        if not s:
            raise Exception("Empty String")

        num = self.string_num_transform(s)

        num_operation = 0
        while num != 0:
            if num & 1 == 1:
                num -= 1
            else:
                num >>= 1
            num_operation += 1
        return num_operation


if __name__ == "__main__":
    p = Problem()

    s = "0100011"
    print(p.calculate_num_operations(s))
