import heapq


class Solution:
    def __init__(self):
        self.tar = None

    def partition(self, arr, low, high, pivot):
        """
        Assume pivot = arr[high]
        """
        i_less = low
        for i in range(low, high):
            if arr[i] <= pivot:  # note the equal
                arr[i], arr[i_less] = arr[i_less], arr[i]
                i_less += 1  # do not forget this
        arr[i_less], arr[high] = arr[high], arr[i_less]  # put the pivot into the mid position
        return i_less

    def q_sort(self, arr, low, high):
        if high - low <= 0:  # high - low <= 0 <==> sub-array length <= 1
            return

        pivot = arr[high]
        mid = self.partition(arr, low, high, pivot)
        self.q_sort(arr, low, mid - 1)  # note index
        self.q_sort(arr, mid + 1, high)  # as above

    def q_select(self, arr, low, high, k):
        if self.tar is not None:  # target found
            return

        pivot = arr[high]
        mid = self.partition(arr, low, high, pivot)

        if k == mid + 1:
            self.tar = arr[mid]
            return
        elif k < mid + 1:
            self.q_select(arr, low, mid - 1, k)
        else:
            self.q_select(arr, mid + 1, high, k)

    def heap_select(self, arr, k):
        """
        Maintain a heap with length == k.
        """
        h = []
        for i in range(len(arr)):
            if i < k:
                heapq.heappush(h, arr[i])
            else:
                heapq.heappush(h, arr[i])
                heapq.heappop(h)
        return h[0]

    def findKthLargest(self, nums: [int], k: int) -> int:
        if not nums:
            raise Exception("Empty Array")

        if k < 0 or k > len(nums):
            raise Exception("Invalid k")

        """
        Sort
        O(NlogN)
        O(logN) - recursion call stack
        """
        # self.q_sort(nums, 0, len(nums) - 1)
        # return nums[-k]

        """
        Heap
        O(NlogK)
        O(logN) - recursion call stack
        """
        # return self.heap_select(nums, k)

        """
        Quick Selection
        O(N)
        O(logN)
        
        1 - kth from end <==> (length - k + 1)th from start
            It is significantly convenient to write if conditions with the latter.
               
        2 - Note the recursion end condition.
            We use self.tar to track whether we should end recursion, which is similar as finding target with DFS.
        """
        # the kth largest <==> the (length - k + 1)th smallest
        self.q_select(nums, 0, len(nums) - 1, len(nums) - k + 1)
        return self.tar


if __name__ == "__main__":
    arr = [3, 2, 1, 5, 6, 4]
    k = 2

    sol = Solution()
    print(sol.findKthLargest(arr, k))
