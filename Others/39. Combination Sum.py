class Solution:
    def __init__(self):
        self.com_set = set()
        self.res = []
        self.path = []

    def DFS(self, arr, tar):
        """
        Brute Force
        Permutation + Distinct
        """
        if tar == 0:
            # Distinct
            # 1 - slice
            # 2 - sort
            # 3 - tuple, list is not hashable
            # 4 - check distinction
            temp = self.path[:]
            temp.sort()
            tu = tuple(temp)
            if tu not in self.com_set:
                self.com_set.add(tu)
                self.res.append(temp)
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

        self.DFS(candidates, target)
        # self.DFS2(candidates, 0, target)
        return self.res
