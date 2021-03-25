class Solution:
    def bs(self, arr, i, j, tar):
        low = i
        high = j

        while low <= high:
            mid = (low + high) >> 1
            if arr[mid] == tar:
                return mid
            elif arr[mid] < tar:
                low = mid + 1
            else:
                high = mid - 1
        return -1

    def search(self, nums: List[int], target: int) -> int:
        """
        Step 1 - Find the start and the end.
        Step 2 - Binary search in the sorted sub-array.

        Notes:
        0 - Corner case: No Rotation, nums[0] < nums[-1]
        1 - Finding start/end: loop condition is high - low > 1, after the loop start = high, end = low
        2 - Search in sub-array: target >= nums[0]/target <= nums[-1], note the equal, covering target == nums[0]
        """
        if not nums:
            # raise Exception("Empty Array")
            return -1

        if nums[0] < nums[-1]:  # no rotation
            return self.bs(nums, 0, len(nums) - 1, target)
        else:
            # find start and end
            low = 0
            high = len(nums) - 1

            while high - low > 1:  # note 1
                mid = (low + high) >> 1
                if nums[mid] > nums[low]:  # low designates the end of the first sub-array(the largest of it)
                    low = mid
                elif nums[mid] < nums[high]:  # high designates the start of the second sub-array(the smallest of it)
                    high = mid

            # check sub-array and implement bs
            if target >= nums[0]:
                return self.bs(nums, 0, low, target)
            elif target <= nums[-1]:
                return self.bs(nums, high, len(nums) - 1, target)
            else:
                return -1  # nums[-1] < target < nums[0]
