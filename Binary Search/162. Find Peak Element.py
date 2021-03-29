class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if not nums:
            raise Exception("Empty Array")
        low = 0
        high = len(nums) - 1

        while low < high:
            # low and high meet at the peak
            mid = (low + high) >> 1
            # while low < high, (mid + 1) never not exceeds
            if nums[mid] > nums[mid + 1]:
                # prune nums[mid + 1:]
                high = mid
            else:
                # prune nums[:mid + 1]
                low = mid + 1
        return low
