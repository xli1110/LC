class Solution:
    def __init__(self):
        self.path = []
        self.res = []

    def DFS(self, arr):
        """
        Sub-Set

        arr = [a, b, c, d]
        path = []

        0 - Going down from a to d.
        1 - path = [a, b, c, d], arr = []
        2 - Pop d, current path = [a, b, c], arr = [], nothing to visit in the for loop.
        3 - Pop c, current arr = [d].
        4 - Visit d, path = [a, b, d].
        Repeat.
        """
        if not arr:
            self.res.append(self.path[:])  # do not forget to append the leaf path
            return

        self.res.append(self.path[:])

        for i, x in enumerate(arr):
            self.path.append(x)
            self.DFS(arr[i + 1:])  # avoid repeatedly using elements before i
            self.path.pop()

    def subsets(self, nums: [int]) -> [[int]]:
        self.DFS(nums)
        return self.res


if __name__ == "__main__":
    sol = Solution()

    arr = [1, 2, 3]

    print(sol.subsets(arr))
