from collections import deque


class Solution:
    def reverseWords(self, s: str) -> str:
        if not s:
            raise Exception("Empty String")

        """
        Built-In Functions - Split, Reverse, Join
        O(N)
        O(N)
        """
        # arr = s.split()[::-1]
        # return " ".join(arr)

        """
        In-Place Swap
        O(N)
        O(1)

        Python can NOT change string values directly like s[i] = ch,
        so we can not implement the in-place swap in Python.
        We use a deque to simulate the changeable string.

        <alpha>
        Example
        s = "MAGA"
        low = 3, high = 3, word = "MAGA"
        Then low += 1, breaking the while loop.
        We do not enqueue the last word.
        """
        low = 0
        high = len(s) - 1

        # remove leading/trailing spaces
        while low <= high:
            if s[low] == " ":
                low += 1
            else:
                break
        while low <= high:
            if s[high] == " ":
                high -= 1
            else:
                break
        if low > high:
            raise Exception("No Word Found")

        # swap
        q = deque()
        word = ""
        while low <= high:
            if s[low] != " ":
                word += s[low]
            else:
                if word:
                    q.appendleft(word)
                    q.appendleft(" ")
                word = ""
            low += 1

        q.appendleft(word)  # <alpha> enqueue the last word manually
        return "".join(q)


if __name__ == "__main__":
    sol = Solution()
    s = "the sky is blue"
    print(sol.reverseWords(s))
