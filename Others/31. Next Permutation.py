class Solution:
    def __init__(self):
        self.res = []
        self.path = []

    def arr_to_num(self, arr):
        s = ""
        for x in arr:
            s += str(x)
        return int(s)

    def find_position(self, nums):
        for i in range(len(self.res)):
            if self.res[i] == nums:
                if i == len(self.res) - 1:
                    return 0

                # we need the check below for duplicate elements in nums
                # run nums = [1, 5, 1] and see the case
                next_num = self.arr_to_num(self.res[i + 1])
                if next_num > self.arr_to_num(nums):
                    return i + 1

        raise Exception("The permutation function has something wrong, please debug it.")

    def DFS(self, arr):
        if not arr:
            self.res.append(self.path[:])
            return

        for i in range(len(arr)):
            self.path.append(arr[i])
            self.DFS(arr[:i] + arr[i + 1:])
            self.path.pop()

    def nextPermutation(self, nums: [int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            raise Exception("Empty Array")

        # all permutations
        # note that we need to SORT the array at first
        arr = nums[:]
        arr.sort()
        self.DFS(arr)

        # find position
        position = self.find_position(nums)

        # in-place replacement
        for i in range(len(nums)):
            nums[i] = self.res[position][i]


if __name__ == "__main__":
    sol = Solution()
    # nums = [2, 1, 3]
    nums = [1, 5, 1]
    sol.nextPermutation(nums)

    print(sol.res)
