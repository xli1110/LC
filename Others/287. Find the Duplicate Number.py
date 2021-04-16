class Solution:
    def hash_check(self, arr):
        """
        O(N)
        O(N)
        """
        s = set()
        for x in arr:
            if x in s:
                return x
            else:
                s.add(x)
        return None

    def pigeonhole(self, arr):
        """
        Request:
        1 - (n - 1) numbers, except for the target, appear once respectively
        2 - target appears twice
        arr = [1, 2, 3, 3, 4], Yes
        arr = [1, 2, 4, 4, 4], No
        O(N)
        O(1)
        """
        for i, x in enumerate(arr):
            if x != i + 1:
                if arr[x - 1] == x:
                    return x
                else:
                    arr[x - 1], arr[i] = arr[i], arr[x - 1]
        return None

    def findDuplicate(self, nums: List[int]) -> int:
        if len(nums) < 2:
            raise Exception("No Duplicates")

        return self.hash_check(nums)
