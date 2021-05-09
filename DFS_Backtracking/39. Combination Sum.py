class Solution:
    def __init__(self):
        self.res = []
        self.path = []

    def DFS(self, arr, tar):
        """
        Combination

        arr = [a, b, c, d]
        path = []

        1 - Fill the path with a, until sum(path) >= tar, say path = [a, a, a, ..., a].
        2 - Pop a, and fill the path with b until sum(path) >= tar, say path = [a, a, a, ..., a, b, b, ..., b].
        3 - Do the same on c and d.
        """
        if not arr:
            return
        if tar < 0:
            return

        if tar == 0:
            self.res.append(self.path[:])

        for i, x in enumerate(arr):
            self.path.append(x)

            # This is WRONG, since we can repeatedly choose each element.
            # self.DFS2(arr[:i] + arr[i + 1:], tar - x)

            self.DFS(arr[i:], tar - x)
            self.path.pop()

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            raise Exception("Empty Candidate List")

        self.DFS(candidates, target)
        return self.res
