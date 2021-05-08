class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        O(N ** 2)
        0 - Avoid searching duplicates for ALL THREE pointers i, low, and high.
        0.0 - For i, use continue.
        0.1 - For low and high, loop as below.
                low += 1
                while low < high and nums[low] == nums[low - 1]:  # avoid duplicates
                    low += 1
                high -= 1
                while low < high and nums[high] == nums[high + 1]:  # avoid duplicates
                    high -= 1
        1 - Sort.
        2 - Fix i, and let two pointers low and high search the target.

        Test Cases
        [-2, 0, 1, 1, 2]
        [-2, 0, 0, 2, 2]
        """
        res = []
        nums.sort()
        for i in range(0, len(nums) - 2):
            if i > 0 and nums[i - 1] == nums[i]:  # avoid duplicates
                continue

            low = i + 1
            high = len(nums) - 1
            while low < high:
                t = nums[i] + nums[low] + nums[high]

                if t == 0:
                    res.append([nums[i], nums[low], nums[high]])
                    low += 1
                    while low < high and nums[low] == nums[low - 1]:  # avoid duplicates
                        low += 1
                    high -= 1
                    while low < high and nums[high] == nums[high + 1]:  # avoid duplicates
                        high -= 1
                elif t < 0:
                    low += 1
                    while low < high and nums[low] == nums[low - 1]:  # avoid duplicates
                        low += 1
                else:
                    high -= 1
                    while low < high and nums[high] == nums[high + 1]:  # avoid duplicates
                        high -= 1
        return res
