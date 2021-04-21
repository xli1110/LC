class Solution:
    def dailyTemperatures(self, T: [int]) -> [int]:
        """
        \alpha
        Explanation of the Equal

        Example
        arr = [2, 3, 3]
        res = [1, 0, 0]

        If we use x > arr[stack[-1]]:
        i = 2, x = 3, stack = [], res = [0, 0, 0], stack = [2]
        i = 1, x = 3, stack = [2], res = [0, 1, 0], stack = [2, 1]
        i = 0, x = 2, stack = [2, 1], res = [1, 1, 0], stack = [2, 1, 0]
        res = [1, 1, 0] - WRONG

        If we use x >= arr[stack[-1]]:
        i = 2, x = 3, stack = [], res = [0, 0, 0], stack = [2]
        i = 1, x = 3, stack = [], res = [0, 0, 0], stack = [1]
        i = 0, x = 2, stack = [1], res = [1, 0, 0], stack = [1, 0]
        res = [1, 0, 0] - RIGHT
        """
        if not T:
            raise Exception("Empty Array")

        stack = []
        res = [0] * len(T)
        i = len(T) - 1
        while i >= 0:  # loop from the end
            # maintain monotonicity
            x = T[i]
            while stack and x >= T[stack[-1]]:  # \alpha
                stack.pop()
            # res
            if stack:
                res[i] = stack[-1] - i
            # push
            stack.append(i)
            # iteration
            i -= 1
        return res


if __name__ == "__main__":
    sol = Solution()

    print(sol.dailyTemperatures([2, 3, 3]))
