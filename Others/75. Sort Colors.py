class Solution:
    def partition(self, arr, low, high):
        pivot = arr[high]
        i_less = low

        for i in range(low, high):
            if arr[i] <= pivot:
                arr[i], arr[i_less] = arr[i_less], arr[i]
                i_less += 1

        arr[i_less], arr[high] = arr[high], arr[i_less]

        return i_less

    def q_sort(self, arr, low, high):
        if high - low < 1:
            return

        i_pivot = self.partition(arr, low, high)

        self.q_sort(arr, low, i_pivot - 1)
        self.q_sort(arr, i_pivot + 1, high)

    def c_sort(self, arr):
        # count
        num0 = 0
        num1 = 0
        num2 = 0
        for x in arr:  # loop 1
            if x == 0:
                num0 += 1
            if x == 1:
                num1 += 1
            if x == 2:
                num2 += 1
        # change
        for i in range(len(arr)):  # loop 2
            if i < num0:
                arr[i] = 0
            elif i < num0 + num1:
                arr[i] = 1
            else:
                arr[i] = 2

    def two_p(self, arr):
        """
        See this url.
        https://leetcode-cn.com/problems/sort-colors/solution/kuai-su-pai-xu-partition-guo-cheng-she-ji-xun-huan/

        p0/p2: The boundary of two zones, say 0 - p0 - 1 and 1 - p2 - 2.
        i: Iteration index.

        interval [a, b) with the form left-closed right-open

        arr[0, p0) == 0
        arr[p0, i) == 1 => When i == 2, the loop terminates. <=> While condition is i < p2.
        arr[p2, len(arr)) == 2


        iteration vs swap
        Who first?
        """
        # init, all intervals must have the length at 0.
        # zero = [0, p0), length == 0
        # one = [p0, i), length == 0
        # two = [p2, len(arr)), length == 0
        p0 = 0
        p2 = len(arr)
        i = 0

        while i < p2:
            if arr[i] == 0:
                # p0 designates the open boundary
                # swap -> iteration
                arr[p0], arr[i] = arr[i], arr[p0]
                p0 += 1
                i += 1
            elif arr[i] == 2:  # do not move the index
                # p2 designates the closed boundary
                # swap -> iteration
                p2 -= 1
                arr[p2], arr[i] = arr[i], arr[p2]
            else:
                i += 1

    def sortColors(self, nums: [int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        """
        Quick Sort
        O(NlogN)
        """
        # self.q_sort(nums, 0, len(nums) - 1)

        """
        Counting Sort
        O(N), loop twice
        """
        # self.c_sort(nums)

        """
        Two Pointers
        O(N), loop once
        """
        self.two_p(nums)


if __name__ == "__main__":
    sol = Solution()

    arr = [2, 0, 2, 1, 1, 0]

    # arr = [1, 2, 0]

    sol.sortColors(arr)

    print(arr)
