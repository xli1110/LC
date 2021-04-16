class Solution:
    def __init__(self):
        self.path = []
        self.num = None

    def DFS(self, arr, tar):
        """
        Brute-Force
        Combination Sum
        See 39
        """
        if not arr:
            return
        if tar == 0:
            if self.num is None:
                self.num = len(self.path)
            else:
                self.num = min(self.num, len(self.path))
            return

        for i, x in enumerate(arr):
            self.path.append(x)
            self.DFS(arr[i:], tar - x)
            self.path.pop()

    def coinChange(self, coins: List[int], amount: int) -> int:

        # self.DFS(coins, amount)
        # return -1 if self.num is None else self.num

