class Solution:
    def __init__(self):
        self.path = []
        self.res = []

    def DFS(self, arr):
        if not arr:
            self.res.append(self.path[:])  # do not forget to append the leaf path
            return

        self.res.append(self.path[:])

        for i, x in enumerate(arr):
            self.path.append(x)
            self.DFS(arr[i + 1:])  # avoid repeatedly using elements before i + 1
            self.path.pop()

    def subsets(self, nums: [int]) -> [[int]]:
        self.DFS(nums)
        return self.res


if __name__ == "__main__":
    sol = Solution()

    arr = [1, 2, 3]

    print(sol.subsets(arr))
