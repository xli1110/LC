class Problem:
    """
    Given a string of different arrows designating to four directions.
    Then we can rotate arrows so that they designate the same direction.

    Example
    "^^<>vvv" -> "^^^^^^^" -> 5 operations
    "^^<>vvv" -> "vvvvvvv" -> 4 operations
    "^^<>vvv" -> ">>>>>>>" -> 6 operations

    Find the minimum number of operations that can rotate them into the same direction.

    Hash Map
    O(N)
    O(1)
    """

    def find_minimum_ope(self, s):
        if not s:
            raise Exception("Empty String")

        d = {
            "^": 0,
            "<": 0,
            "v": 0,
            ">": 0,
        }

        for ch in s:
            if ch in d:
                d[ch] += 1
            else:
                raise Exception("Invalid Character {}".format(ch))

        return len(s) - max(d.values())


if __name__ == "__main__":
    p = Problem()
    s = "^^<>vvv"
    print(p.find_minimum_ope(s))
