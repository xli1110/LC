class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        O(N ** 2)
        0 - Avoid searching duplicates for ALL THREE pointers i, low, and high.
        0.0 - For i, use continue.
        0.1 - For low and high, loop as below.
              There is no need to search in [i, len(nums) - 1], instead searching from high or low.

               j = low + 1
               while j < high and nums[j] == nums[low]:  # note that J < HIGH
                   j += 1
               low = j

        1 - Sort.
        2 - Fix i, and let two pointers low and high search the target.
        """
        res = []
        nums.sort()
        for i in range(0, len(nums) - 2):
            if i > 0 and nums[i - 1] == nums[i]:  # avoid duplicates
                continue

            low = i + 1
            high = len(nums) - 1
            while high > low:
                # Test Cases
                # [-2, 0, 1, 1, 2]
                # [-2, 0, 0, 2, 2]
                t = nums[i] + nums[low] + nums[high]
                if t == 0:
                    res.append([nums[i], nums[low], nums[high]])

                    j = low + 1
                    while j < high and nums[j] == nums[low]:  # avoid duplicates
                        j += 1
                    low = j

                    j = high - 1
                    while j > low and nums[j] == nums[high]:  # avoid duplicates
                        j -= 1
                    high = j
                elif t < 0:
                    j = low + 1
                    while j < high and nums[j] == nums[low]:  # avoid duplicates
                        j += 1
                    low = j
                else:
                    j = high - 1
                    while j > low and nums[j] == nums[high]:  # avoid duplicates
                        j -= 1
                    high = j
        return res
