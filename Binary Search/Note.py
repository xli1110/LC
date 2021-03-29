"""
Tips:
- mid = (low + high) >> 1
- high == low + 1 <==> mid == low


1 - Basic Binary Search
    Search the index of a target in a given sorted array.

    Problems:
    374, 704

    Loop Condition:
    low <= high
    Two pointers cross over after loop, like [x, x, x, x, high, low, x, x, x].
    Note that pointers may EXCEED after loop, like high -> -1 or low -> len(arr).

    Iteration:
    temp = f[mid]
    if temp == tar:
        return mid
    elif temp < tar:
        low = mid + 1
    else:
        high = mid - 1

    Return after Loop:
    return -1(Target not Found)

1' - Tricky Binary Search
    Can test some concrete cases.

    Problems:
    69 - find the FLOOR of sqrt(x), after loop, high designates the floor.


2 - Partially Binary Search
    Search the start of the second sub-array and the end of the first sub-array.
    high -> start, low -> end

    Problems:
    33, 153, 278

    Loop Condition:
    high - low > 1
    Two pointers stop as ordered neighbors after loop. [x, x, x, x, low, high, x, x, x]

    Iteration:
    if f[mid] > f[low]:
        low = mid
    elif f[mid] < f[high]:
        high = mid

    Return after Loop:
    return low/high

4 - Others
    34 - search start/end RESPECTIVELY
    162 - not sorted, compare arr[mid] and arr[mid + 1] and prune redundant part, while low < high
    658 - note indices exceeding cases
"""
