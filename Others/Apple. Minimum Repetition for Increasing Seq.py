"""
2021 - 06 - 10
Perfect Interviewer - Nice Coding Hints, Considerate Interview Scheduling



Problem:
Given an integer array with distinct elements, we can repeat it N times.
How to find the minimum N to get the longest increasing sequence?
What if there exist repeating elements?



Example 1:
arr = [9, 8, 7, 2, 3, 6, 4]
answer = 5

[9, 8, 7, !2, !3, 6, !4] [9, 8, 7, 2, 3, !6, 4] [9, 8, !7, 2, 3, 6, 4] [9, !8, 7, 2, 3, 6, 4] [!9, 8, 7, 2, 3, 6, 4]
The longest increasing sequence is marked with an exclamation.
seq = 2, 3, 4, 6, 7, 8, 9
N = 5



Example 2:
arr = [4, 1, 5, 2, 6, 3]
answer = 2

[4, !1, 5, !2, 6, !3] [!4, 1, !5, 2, !6, 3]
The longest increasing sequence is marked with an exclamation.
seq = 1, 2, 3, 4, 5, 6
N = 2
"""


def num_min_repeat(arr):
    """
    Discuss the length of the longest increasing sequence.
    length = the number of distinct elements

    Use an end to store the last element's index of the seq.

    Loop the sorted array temp(monotonically increasing), and let index = arr.index(x).
    (interviewer helped me modify the update rule)
    case 1: index > end => we can append x after end and hold the monotonicity
    case 2: index < end => we need a repetition to append x after end, num += 1

    Update end as end <- index.

    If elements are not distinct.
    <a> temp = set(arr)
    <b> we may find multi matches as indices = [i1, i2, i3, ..., iN], where i1 < i2 < ... < iN
        case 1: end < i1, use i1 to update end
        case 2: end > iN, we need a repetition, use i1 to update end
        case 3: i1 < end < iN, use the smallest i which is greater than end to update end
    """
    if not arr:
        raise Exception("Empty Array")

    # sort
    temp = arr[:]  # <a>
    temp.sort()

    # init
    num = 1
    end = arr.index(temp[0])  # pick the minimum index

    # loop
    for i in range(1, len(temp)):
        # find index
        x = temp[i]
        index = arr.index(x)  # <b>
        # need a repetition
        if index < end:
            num += 1
        # update
        end = index

    return num


"""
The interviewer asks me to write some test cases, especially those corner cases.
"""
# arr = [9, 8, 7, 2, 3, 6, 4]
# arr = [4, 1, 5, 2, 6, 3]
# arr = []
# arr = [1, 2, 3]
# arr = [3, 2, 1]
arr = [1, 3, 2, 3]
print(num_min_repeat(arr))
