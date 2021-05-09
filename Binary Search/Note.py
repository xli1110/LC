"""
Tips:
    - tar > arr[mid], put tar before arr[mid] for easier understanding
    - mid = (low + high) >> 1
    - high - low == 1 <==> mid == low



1 - Basic Binary Search
    Two pointers cross over after loop, like [x, x, x, x, high, low, x, x, x].

    Note that pointers may EXCEED after loop, like high -> -1 or low -> len(arr).
    In conclusion, low \in {0, 1, 2, ..., len(arr)}, high \in {-1, 0, 1, ..., len(arr) - 1}.

    Model:
    while low <= high
        temp = arr[mid]
        if tar == temp:
            return mid
        elif tar > temp:
            low = mid + 1
        else:
            high = mid - 1
    return None  # Target not Found

    Problems:
    270(BST)
    367(perfect square)
    374(BS)
    704(BS)



1' - Tricky Binary Search
    Test some concrete cases.

    Problems:
    35(insert) - search the (floor + 1) of tar, after loop, low designates floor + 1
    69(sqrt) - search the FLOOR of sqrt(x), after loop, high designates the floor.



2 - Partially Binary Search
    Two pointers stop as ordered neighbors after loop, like [x, x, x, x, low, high, x, x, x].
    Then, high -> START of the second sorter sub-array, low -> END of the first.

    Model:
    # NOTE THIS CASE, NO ROTATION
    if arr[0] < arr[-1]:
        return arr[0]

    while high - low > 1:
        mid = (low + high) >> 1
        if arr[mid] > arr[low]:
            low = mid
        elif f[mid] < f[high]:
            high = mid

    Problems:
    33(rotation)
    153(rotation)
    278(partially sorted)



3 - Others
    34(repeated elements) - search start/end RESPECTIVELY
    50(power) - divide it into two cases by the INDEX (base ^ index)
    162(peak) - while low < high, compare arr[mid] and arr[mid + 1]; PRUNE redundant part
    658(closest elements) - note indices exceeding cases
    702(unknown length) - assume 19999 is the maximum length of the array
"""
