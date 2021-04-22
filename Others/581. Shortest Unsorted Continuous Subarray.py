class Solution:

    def findUnsortedSubarray(self, nums: [int]) -> int:
        if len(nums) <= 1:
            return 0
        low = None
        high = None

        temp = nums[:]
        temp.sort()

        i = 0
        while i <= len(nums) - 1:
            if nums[i] != temp[i]:
                low = i
                break
            i += 1

        i = len(nums) - 1
        while i >= 0:
            if nums[i] != temp[i]:
                high = i
                break
            i -= 1

        return 0 if low is None else high - low + 1


if __name__ == "__main__":
    # arr = [1, 5, 3, 2, 4]
    arr = [1, 2, 3]
    # arr = [3, 2, 1]
    sol = Solution()
    print(sol.findUnsortedSubarray(arr))
