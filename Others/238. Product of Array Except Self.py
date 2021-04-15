class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) < 2:
            raise Exception("Invalid Array")

        pre_prod = [1] * len(nums)
        post_prod = [1] * len(nums)
        res = [None] * len(nums)

        i = 1
        while i <= len(nums) - 1:
            pre_prod[i] = pre_prod[i - 1] * nums[i - 1]
            i += 1
        i = len(nums) - 2
        while i >= 0:
            post_prod[i] = post_prod[i + 1] * nums[i + 1]
            i -= 1

        for i in range(len(nums)):
            res[i] = pre_prod[i] * post_prod[i]
        return res
