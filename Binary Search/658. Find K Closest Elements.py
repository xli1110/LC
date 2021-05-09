class Solution:
    def findClosestElements(self, arr: [int], k: int, x: int) -> [int]:
        """
        O(logN + k)
        O(k)

        step 0 - Corner Cases
        step 1 - binary search the target
        step 2 - determine the closest position, be careful for exceeding cases
        step 3 - BFS starts at the position, note the loop condition
        """
        # step 0 - corner cases
        if not arr:
            raise Exception("Empty Array")
        if k > len(arr) or k < 0:
            raise Exception("Invalid k, {0} > length of array.".format(k))
        if k == 0:
            return []

        # step 1 - binary search
        low = 0
        high = len(arr) - 1
        has_found = False
        while low <= high:
            mid = (low + high) >> 1
            if arr[mid] == x:
                has_found = True
                break
            elif arr[mid] < x:
                low = mid + 1
            else:
                high = mid - 1

        # step 2 - determine the position of the closest position
        if has_found:
            position = mid
        else:
            # check pointer exceeding
            if high < 0:
                position = low
            elif low > len(arr) - 1:
                position = high
            else:
                # note 1 - after loop, low > high always holds
                # note 2 - we use strictly less, arr = [1, 3], tar = 2, we should return 1 as requested
                position = low if abs(arr[low] - x) < abs(arr[high] - x) else high

        # step 3 - BFS
        # search the result with two pointers
        # initialize as [..., low, position, high, ...]
        # return res = arr[low + 1:high] at last
        low = position - 1
        high = position + 1
        while low >= 0 and high <= len(arr) - 1:
            if high - low - 1 == k:
                return arr[low + 1: high]

            v_low = abs(arr[low] - x)
            v_high = abs(arr[high] - x)

            if v_high < v_low:
                high += 1
            else:
                low -= 1

        if low < 0:
            return arr[:k]
        else:
            return arr[len(arr) - k:]


if __name__ == "__main__":
    sol = Solution()
    # print(sol.findClosestElements([1, 3], 1, 2))
    print(sol.findClosestElements([1, 1, 1, 10, 10, 10], 1, 9))
