class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        dp[i] denotes the max sub-array ending at i.
        dp[i] = nums[i], if dp[i - 1] < 0
                dp[i - 1] + nums[i], else
        """
        if not nums:
            raise Exception("Empty Array")

        dp = [nums[0]]

        for i in range(1, len(nums)):
            if dp[i - 1] < 0:
                dp.append(nums[i])
            else:
                dp.append(dp[i - 1] + nums[i])

        return max(dp)
