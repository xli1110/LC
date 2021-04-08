class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if not nums:
            raise Exception("Empty List")

        d = {}
        for x in nums:
            if x in d:
                d[x] += 1
            else:
                d[x] = 1
            if d[x] > len(nums) / 2:
                return x
        return None
