class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if not nums:
            raise Exception("Empty Array")

        res = nums[0]
        for i in range(1, len(nums)):
            res ^= nums[i]

        return res
