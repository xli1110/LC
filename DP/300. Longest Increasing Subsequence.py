class Solution:
    def brute_force(self, arr):
        """
        It does not work.
        Example
        arr = [0, 1, 0, 3, 2, 3]
        i = 0, j = 3, arr[j] = 3, max_length = 3, [0, 1, 3], temp_max = 3;
        j = 4, arr[j] = 2 < temp_max, the last two elements will not be considered;
        but the real answer is [0, 1, 2, 3].
        """
        max_length = 1
        for i in range(len(arr)):
            temp_length = 1
            temp_max = arr[i]
            for j in range(i + 1, len(arr)):
                if arr[j] > temp_max:
                    temp_max = arr[j]
                    temp_length += 1
            if temp_length > max_length:
                max_length = temp_length
        return max_length

    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            raise Exception("Empty Array")

        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    # we update dp[i] only if we can TRANSFER from arr[j] to arr[i]
                    # which implies that arr[j] < arr[i]
                    # otherwise, dp[i] = 1
                    temp_max = dp[j] + 1
                    if temp_max > dp[i]:
                        dp[i] = temp_max

        return max(dp)
