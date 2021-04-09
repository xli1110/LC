class Solution:
    def __init__(self):
        self.dic = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        self.path = []
        self.res = []

    def DFS(self, digits, low):
        """
        1 - Base Case
            Have visited all digits.
            Store the path.
            self.res.append("".join(self.path))

        2 - Search the letters associated with the current digit.
            digit = digits[low]
            arr = dic[digit]

        3 - Loop its children.
            for char in arr:
                self.path.append(char)
                self.DFS(digits, low + 1)
                self.path.pop()
        """
        if low >= len(digits):  # search completed
            self.res.append("".join(self.path))  # arr to str - s = "".join(arr)
            return

        digit = digits[low]

        if digit not in self.dic:  # invalid input protection
            raise Exception("Invalid Input {0}".format(digit))

        for char in self.dic[digit]:  # traverse children
            self.path.append(char)
            self.DFS(digits, low + 1)
            self.path.pop()

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        self.DFS(digits, 0)
        return self.res
