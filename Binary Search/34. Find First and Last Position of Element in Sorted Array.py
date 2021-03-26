class Solution:
    def search_start(self, arr, tar):
        low = 0
        high = len(arr) - 1
        while low <= high:
            mid = (low + high) >> 1
            if arr[mid] == tar:
                if mid == 0 or arr[mid - 1] != tar:
                    return mid
                high = mid - 1
            elif arr[mid] < tar:
                low = mid + 1
            else:
                high = mid - 1
        return -1

    def search_end(self, arr, tar):
        low = 0
        high = len(arr) - 1
        while low <= high:
            mid = (low + high) >> 1
            if arr[mid] == tar:
                if mid == len(arr) - 1 or arr[mid + 1] != tar:
                    return mid
                low = mid + 1
            elif arr[mid] < tar:
                low = mid + 1
            else:
                high = mid - 1
        return -1

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            # raise Exception("Empty Array")
            return [-1, -1]

        res = []

        # search start
        start = self.search_start(nums, target)
        res.append(start)

        # corner case: target not found
        if start == -1:
            return [-1, -1]

        # search end
        end = self.search_end(nums,target)
        res.append(end)

        return res
