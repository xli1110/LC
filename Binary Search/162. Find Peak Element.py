class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if not nums:
            raise Exception("Empty Array")

        low = 0
        high = len(nums) - 1

        while low < high:
            # low and high meet at the peak
            mid = (low + high) >> 1
            # while low < high, (mid + 1) never exceeds, so we can safely visit nums[mid + 1]
            if nums[mid] > nums[mid + 1]:
                # PRUNE nums[mid + 1:]
                high = mid
            else:
                # PRUNE nums[:mid + 1]
                low = mid + 1
        return low
