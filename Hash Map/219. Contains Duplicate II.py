class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = {}
        for i, x in enumerate(nums):
            if x in dic:
                if abs(dic[x] - i) <= k:
                    return True
            dic[x] = i
        return False
