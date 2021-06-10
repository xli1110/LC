"""
2021 - 06 - 10
Perfect Interviewer - Nice Coding Hints, Considerate Interview Scheduling



Given an array, return the length of the longest increasing sub-sequence.



Example 1:
arr = [5, 6, 2, 7, 9, 9, 9]
output = 4
seq = [5, 6, 7, 9]



Example 2:
arr = [7, 7, 7, 7, 7]
output = 1
seq = [7]
"""


def longest_increasing_sub_seq(arr):
    """
    Ask the data type and corner cases.
    Interviewer says as below.
    - arr is not empty
    - all element is INT

    Let dp[i] denote the length of the longest increasing sequence ending at i.
    Search arr[j] < arr[i] where j in range(i).

    If not exist such j: dp[i] = 1
    Else: dp[i] = dp[j] + 1

    Interviewer: What if there are multi matches?
    Modification: Transfer from the maximum dp[j], because dp[i] records the LONGEST sub-seq.
    """
    # init
    dp = [1] * len(arr)

    # loop
    for i in range(len(dp)):
        potential_seq_length = -1
        for j in range(i):
            # we can transfer from j to i if arr[j] < arr[i]
            if arr[j] < arr[i]:
                # If there are more than one j, which one the transfer should start at?
                # The j which has the maximum dp[j].
                if dp[j] > potential_seq_length:
                    potential_seq_length = dp[j]

        if potential_seq_length < 0:  # no such j found
            dp[i] = 1
        else:  # transfer
            dp[i] = potential_seq_length + 1

    return max(dp)


arr = [5, 6, 2, 7, 9, 9, 9]
# arr = [7, 7, 7, 7, 7]
print(longest_increasing_sub_seq(arr))
