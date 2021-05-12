"""
Q: Suppose we have an unsorted array,
return the maximum length of the continuous sequence.

For example:
Input: 5, 7, 100, 6, 4, 11, 10, 15
Output: 4(If we sort it, it should be: 4, 5, 6, 7, 10, 11, 15, 100)
As 4, 5, 6, 7 is the maximum continuous sequence.

Requirements:
O(N) Time

Ask: Element type.
Ans: Integer.
This implies hash map search d[x - 1] and d[x + 1].
"""


def max_continuous_length(arr):
    if not arr:
        raise Exception("Empty Array")

    max_length = 1

    d = {x: [1, False, False] for x in arr}
    # [num_continuous, add from previous, add from next]

    for key in d:
        if key - 1 in d:
            if not d[key - 1][2]:
                d[key][0] += d[key - 1][0]
                d[key][1] = True
        if key + 1 in d:
            if not d[key + 1][1]:
                d[key][0] += d[key + 1][0]
                d[key][2] = True

        if d[key][0] > max_length:
            max_length = d[key][0]

    return max_length


print(max_continuous_length([5, 7, 100, 6, 4, 11, 10, 15]))
