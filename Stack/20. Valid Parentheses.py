class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        left = ["(", "[", "{"]
        right = [")", "]", "}"]

        for char in s:
            if char in left:
                stack.append(char)
            elif char in right:
                if not stack:
                    return False

                x = stack.pop()

                if x not in left:
                    return False
                if left.index(x) != right.index(char):
                    return False

        return not stack
