class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        1 - Generate a Dictionary
        dic[x] = [indices], s.t. pre_sum[index] = x

        2 - Search the Answer
        sum(arr[i + 1:j + 1]) == k
        <=> pre_sum[j] - pre_sum[i] == k
        <=> pre_sum[j] - pre_sum[i] == k
        <=> pre_sum[j] - k in dic

        for i, x in enumerate(arr),
        d[x] = [indices] implies potential sub-arrays arr[index + 1:i + 1] with sum == k.

        Note we do not need to consider exceeding case like index > i,
        since we only loop once which ensemble both generation and search.
        """
        if not nums:
            raise Exception("Empty Array")

        res = 0
        dic = {}
        pre_sum = 0
        for i, x in enumerate(nums):
            pre_sum += x

            # search target
            if pre_sum == k:
                res += 1
            if pre_sum - k in dic:
                res += len(dic[pre_sum - k])

            # upgrade the dic
            if pre_sum not in dic:
                dic[pre_sum] = [i]
            else:
                dic[pre_sum].append(i)

        return res
