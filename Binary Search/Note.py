"""
Tips:
    - tar > arr[mid], put tar before arr[mid] for clearer understanding
    - mid = (low + high) >> 1
    - high - low == 1 <==> mid == low


1 - Basic Binary Search
    Search the index of a target in a given sorted array.

    Problems:
    270(BST)
    367(perfect square) - 69
    374(BS)
    704(BS)

    Loop Condition:
    low <= high
    Two pointers cross over after loop, like [x, x, x, x, high, low, x, x, x].
    Note that pointers may EXCEED after loop, like high -> -1 or low -> len(arr).
    In conclusion, low in {0, 1, 2, ..., len(arr)}, high in {-1, 0, 1, ..., len(arr) - 1}.

    Iteration:
    temp = f[mid]
    if tar == temp:
        return mid
    elif tar > temp:
        low = mid + 1
    else:
        high = mid - 1

    Return after Loop:
    return -1(Target not Found)

1' - Tricky Binary Search
    Can test some concrete cases.

    Problems:
    35(insert) - search the (floor + 1) of tar, after loop, low designates floor + 1
    69(sqrt) - search the FLOOR of sqrt(x), after loop, high designates the floor.


2 - Partially Binary Search
    Search the start of the second sub-array and the end of the first sub-array.
    high -> start, low -> end

    Problems:
    33(rotation), 153(rotation), 278(partially sorted)

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

3 - Others
    34(repeated elements) - search start/end RESPECTIVELY
    50(power) - divide it into two cases by the index (base ^ index)
    162(peak) - not sorted, compare arr[mid] and arr[mid + 1] and prune redundant part, while low < high
    658(closest elements) - note indices exceeding cases
    702(unknown length) - assume 19999 is the maximum length of the array
"""
