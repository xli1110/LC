class Solution:
    def __init__(self):
        self.res = []
        self.path = []

    def DFS(self, arr, tar):
        """
        This is actually the PERMUTATION of the target.
        Can not remove duplicate combinations.
        arr = [2, 3], tar = 7
        res = [[2,2,3], [2,3,2], [3,2,2]]
        """
        if tar == 0:
            self.res.append(self.path[:])
            return
        if tar < 0:
            return

        for x in arr:
            self.path.append(x)
            self.DFS(arr, tar - x)
            self.path.pop()

    def DFS2(self, arr, low, tar):
        """
        Combination
        """
        if low >= len(arr):
            return
        if tar < 0:
            return
        if tar == 0:
            self.res.append(self.path[:])
            return

        self.path.append(arr[low])
        self.DFS2(arr, low, tar - arr[low])
        self.path.pop()
        self.DFS2(arr, low + 1, tar)

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            raise Exception("Empty Candidate List")

        self.DFS2(candidates, 0, target)
        return self.res
