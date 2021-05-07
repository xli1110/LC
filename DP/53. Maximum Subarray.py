class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        dp[i] denotes the max sub-array ending at i.
        dp[i] = max(dp[i - 1] + nums[i], nums[i])
        """
        if not nums:
            raise Exception("Empty Array")

        dp = [None] * len(nums)
        dp[0] = nums[0]

        for i in range(1, len(nums)):
            dp[i] = nums[i]
            if dp[i - 1] > 0:
                dp[i] += dp[i - 1]

        return max(dp)
