class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        """
        Bubble Sort
        O(N ** 2)
        """
        # for i in range(len(nums)):
        #     for j in range(len(nums) - 1):
        #         if nums[j] == 0 and nums[j + 1] != 0:
        #             nums[j], nums[j + 1] = nums[j + 1], nums[j]

        """
        Two Pointers - Quick Sort Partition
        O(N)
        """
        i_non = 0  # non-zero elements
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i_non], nums[i] = nums[i], nums[i_non]
                i_non += 1  # i_non designates the first zero
