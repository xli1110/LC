class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = {}
        res = []

        for x in nums1:
            if x in d:
                d[x] += 1
            else:
                d[x] = 1

        for x in nums2:
            if x in d:
                if d[x] > 0:
                    # note this modification
                    res.append(x)
                    d[x] -= 1

        return res
