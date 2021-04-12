class Solution:
    def __init__(self):
        self.path = []
        self.res = []

    def DFS(self, arr):
        if not arr:  # base case, all elements permuted
            self.res.append(self.path[:])
            return
        for i in range(len(arr)):
            self.path.append(arr[i])
            self.DFS(arr[:i] + arr[i + 1:])
            self.path.pop()

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.DFS(nums)
        return self.res
