class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            raise Exception("Empty Array")

        if nums[0] < nums[-1]:  # no rotation
            return nums[0]

        low = 0
        high = len(nums) - 1
        while high - low > 1:
            mid = (low + high) >> 1
            if nums[low] < nums[mid]:
                low = mid
            elif nums[high] > nums[mid]:
                high = mid

        return nums[high]
