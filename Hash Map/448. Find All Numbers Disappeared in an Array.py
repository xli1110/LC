class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        if len(nums) < 1:
            raise Exception("Invalid Array")

        n = len(nums)
        res = []
        s = set()

        for x in nums:
            s.add(x)

        for i in range(1, n + 1):
            if i not in s:
                res.append(i)

        return res
