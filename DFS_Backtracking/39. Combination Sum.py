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

    def DFS2(self, arr, tar):
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
        if tar < 0:  # do not forget this case
            return
        if tar == 0:
            self.res.append(self.path[:])
            return

        for i, x in enumerate(arr):
            self.path.append(x)

            # This is WRONG, since we can repeatedly choose each element.
            # self.DFS2(arr[:i] + arr[i + 1:], tar - x)

            self.DFS2(arr[i:], tar - x)
            self.path.pop()

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            raise Exception("Empty Candidate List")

        # self.DFS(candidates, target)

        self.DFS2(candidates, target)

        return self.res
