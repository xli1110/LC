class Solution:
    def __init__(self):
        self.num = 0

    def DFS(self, arr, tar):
        if not arr:
            if tar == 0:
                self.num += 1
            return

        for i, x in enumerate(arr):
            self.DFS(arr[i + 1:], tar - x)
            self.DFS(arr[i + 1:], tar + x)

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        return self.num
