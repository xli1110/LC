class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            raise Exception("Empty Array")

        right_most = 0

        i = 0
        while i <= len(nums) - 1:
            if i > right_most:
                # we can not reach i
                # nums = [3, 2, 1, 0, 4], i = 4, right_most = 3
                return False

            if i + nums[i] > right_most:
                # update right_most
                right_most = i + nums[i]

            if right_most >= len(nums) - 1:
                # we can reach the last element
                return True

            i += 1  # do not forget iterate the index

        return False
