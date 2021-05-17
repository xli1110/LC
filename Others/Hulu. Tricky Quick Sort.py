class Problem:
    """
    Assume we have two lists of screws and bolts respectively as below.
    screw = [s1, s2, ..., sN]
    bolt = [b1, b2, ..., bN]
    Each array's elements are distinct and there exist one and only one bolt b[j] that matched the screw s[i].

    We are provided a judge function, judge(i, j), that check whether s[i] and b[j] matches.
    judge(i, j) < 0 if s[i] < b[j]
    judge(i, j) == 0 if s[i] matches b[j]
    judge(i, j) > 0 if s[i] > b[j]

    Since all screws have similar sizes, we can not directly compare them, say we do not know whether s[i] > s[j].
    How to match each screw-bolt pair ASAP?

    I - We can not sort the array, right?
    Int - Exactly.
    I - For each screw, we can judge all bolts. This has O(N ** 2) complexity.
    Int - Yes, can we be faster?

    Think

    Int - When we match s[i] and b[j], can we know which bolts are larger/smaller then b[j]?
    I - Yes, we can let b[j] be the pivot and invoke judge(i, j) on other bolts to find smaller/larger bolts.
        This seems like quick sort partition.
    Int - Yes, we can recursively invoke the method.
          Can we do the same thing on screws?
    I - We can at first partition screws, and then partition bolts.
        Like below.
        screw = [Less1] + [mid1] + [Great1]
        Pick s[mid1] as the new pivot to partition bolts.
        bolt = [Less2] + [mid2] + [Great2]
        We have s[mid1] matches b[mid2], Less1 matches Less2, and Great1 matches Great2.
        This method needs O(NlogN) time.
    Int - Ask some quick sort problems, like best/average/worst time, pivot selection, etc.
    """

    def __init__(self):
        self.arr1 = [1, 3, 4, 5, 2]
        self.arr2 = [5, 2, 4, 3, 1]

    def judge(self, i, j):
        return self.arr1[i] - self.arr2[j]

    def partition1(self, arr, low, high, i_pivot):
        """
        Partition Screws
        """
        i_less = low
        for i in range(low, high + 1):
            if self.judge(i, i_pivot) <= 0:
                arr[i], arr[i_less] = arr[i_less], arr[i]
                if self.judge(i_less, i_pivot) == 0:  # record the mid value's position
                    i_match = i_less
                i_less += 1
        arr[i_less - 1], arr[i_match] = arr[i_match], arr[i_less - 1]  # put the pivot into the mid position
        return i_less - 1

    def partition2(self, arr, low, high, i_pivot):
        """
        Partition Bolts
        """
        i_less = low
        for i in range(low, high + 1):
            if self.judge(i_pivot, i) >= 0:
                arr[i], arr[i_less] = arr[i_less], arr[i]
                if self.judge(i_less, i_pivot) == 0:
                    i_match = i_less
                i_less += 1
        arr[i_less - 1], arr[i_match] = arr[i_match], arr[i_less - 1]  # put the pivot into the mid position
        return i_less - 1

    def q_sort(self, arr1, arr2, low1, high1, low2, high2):
        if low1 >= high1 or low2 >= high2:
            return

        # partition arr1 based on pivot
        mid1 = self.partition1(arr1, low1, high1, high2)  # randomly select a bolt from arr2 as high2
        # partition arr2 based on mid1
        mid2 = self.partition2(arr2, low1, high1, mid1)

        self.q_sort(arr1, arr2, low1, mid1 - 1, low2, mid2 - 1)
        self.q_sort(arr1, arr2, mid1 + 1, high1, mid2 + 1, high2)


if __name__ == "__main__":
    p1 = Problem()
    p1.q_sort(p1.arr1, p1.arr2, 0, len(p1.arr1) - 1, 0, len(p1.arr2) - 1)

    print(p1.arr1)
    print(p1.arr2)
