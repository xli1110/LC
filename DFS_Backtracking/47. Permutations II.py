class Solution:
    def __init__(self):
        self.path = []
        self.res = set()

    def DFS(self, arr):
        """
        46 + Tuple
        """
        if not arr:
            self.res.add(tuple(self.path))
            return

        for i in range(len(arr)):
            self.path.append(arr[i])
            self.DFS(arr[:i] + arr[i + 1:])
            self.path.pop()

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            raise Exception("Empty Array")

        self.DFS(nums)
        res_list = [list(x) for x in self.res]
        return res_list
