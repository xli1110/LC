class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        Think:
        The insert index is in {0, 1, 2, ..., len(arr)}
        Coincidentally, low also designates {0, 1, 2, ..., len(arr)} after the loop.

        nums = [1, 3, 5, 7, 9], tar = 8
        1 - low = 0, high = 4, mid = 2, 5 < 8
        2 - low = 3, high = 4, mid = 3, 7 < 8
        3 - low = 4, high = 4, mid = 4, 9 > 8
        4 - low = 4, high = 3, return low = 4

        nums = [1, 3, 5, 7, 9], tar = 10
        1 - low = 0, high = 4, mid = 2, 5 < 10
        2 - low = 3, high = 4, mid = 3, 7 < 10
        3 - low = 4, high = 4, mid = 4, 9 < 10
        4 - low = 5, high = 4, return low = 5

        nums = [1, 3, 5, 7, 9], tar = -1
        1 - low = 0, high = 4, mid = 2, 5 > -1
        2 - low = 0, high = 1, mid = 0, 1 > -1
        3 - low = 0, high = -1, return low = 0
        """
        if not nums:
            return 0

        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) >> 1
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return low
