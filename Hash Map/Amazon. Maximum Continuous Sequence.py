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
    """
    init
    d = {x: [x, x] for x in arr}

    key = element
    val = [start val of the continuous seq, end val of the continuous seq]

    Example:
    arr = [1, 3, 0, -1]
    After we loop the array, we have:
    d[3] = [3, 3]
    d[1] = [-1, 1]
    d[0] = [-1, 1]
    d[-1] = [-1, 1]
    So the maximum length is (1 - (-1)) + 1 = 3.
    """
    if not arr:
        raise Exception("Empty Array")

    # init
    max_length = 1
    d = {x: [x, x] for x in arr}

    for key in d:
        # add from pre
        if key - 1 in d:
            d[key][0] = d[key - 1][0]  # update cur's start
            d[key - 1][1] = d[key][1]  # update pre's end

        # add from next
        if key + 1 in d:
            d[key][1] = d[key + 1][1]  # update cur's end
            d[key + 1][0] = d[key][0]  # update next's start

        # update max val
        temp = d[key][1] - d[key][0] + 1
        if temp > max_length:
            max_length = temp

    return max_length


if __name__ == "__main__":
    arr = [5, 7, 100, 6, 4, 11, 10, 15, 3, 2]
    print(max_continuous_length(arr))
