class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            raise Exception("Empty Array")
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        # loop arr[0:N - 1]
        dp_0 = [0] * len(nums)
        dp_0[0] = nums[0]
        dp_0[1] = max(nums[0], nums[1])

        for i in range(2, len(nums) - 1):
            dp_0[i] = max(dp_0[i - 1], dp_0[i - 2] + nums[i])

        # loop arr[1:N]
        dp_1 = [0] * len(nums)
        dp_1[1] = nums[1]
        dp_1[2] = max(nums[1], nums[2])

        for i in range(3, len(nums)):
            dp_1[i] = max(dp_1[i - 1], dp_1[i - 2] + nums[i])

        return max(max(dp_0), max(dp_1))
