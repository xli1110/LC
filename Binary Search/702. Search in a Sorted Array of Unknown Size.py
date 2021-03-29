"""
Given an integer array sorted in ascending order, write a function to search target in nums.
If target exists, then return its index, otherwise return -1.
However, the array size is unknown to you.
You may only access the array using an ArrayReader interface, where ArrayReader.get(k) returns the element of the array at index k (0-indexed).

You may assume all integers in the array are less than 10000, and if you access the array out of bounds, ArrayReader.get will return 2147483647.
"""


class Solution:
    def search(self, reader, target):
        if reader.get(0) == 2147483647:
            # raise Exception("Empty Array")
            return -1  # not found

        if target > 9999 or target < -9999:
            return -1

        low = 0
        high = 19998  # there are at most 19999 elements in the array
        while low <= high:
            mid = (low + high) >> 1
            if reader.get(mid) == target:
                return mid
            elif target > reader.get(mid):
                # mid is a valid index and target > arr[mid]
                low = mid + 1
            else:
                # mid is an invalid index or mid is valid and target < arr[mid]
                high = mid - 1
        return -1
