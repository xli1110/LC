"""
----Easy----

283. Move Zeroes - <Counting Sort, Two Pointers Partition>

461. Hamming Distance - <Bitwise Operation>
     Similar Problems:
     2. Add Two Numbers
     21. Merge Two Sorted Lists



----Medium----

5. Longest Palindromic Substring - <Two Pointers, Central Expansion>
   Notes:
   1 - The center has (N + N - 1) potential positions, not N.
   2 - return s[low + 1:high].
   3 - No need to distinguish index exceeding or digit difference.

11. Container With Most Water - <Two Pointers>

15. 3Sum - <Sort, Two Pointers, Duplicates>

17. Letter Combinations of a Phone Number - <DFS, Backtracking>
    Similar Problems:
    112. Path Sum
    Notes:
    1 - Base Case
        Have visited all digits.
        Store the path.
        self.res.append("".join(self.path))

    2 - Search the letters associated with the current digit.
        digit = digits[low]
        arr = dic[digit]

    3 - Loop its children.
        for char in arr:
            self.path.append(char)
            self.DFS(digits, low + 1)
            self.path.pop()

22. Generate Parentheses - <DFS, Backtracking>

31. Next Permutation - <DFS, Backtracking, Permutation>
    Notes:
    1 - Apply brute-force method to find all permutations and the next one, but the executing time exceeds.

39. Combination Sum - <DFS, Backtracking, Combination, Permutation + Distinct>
    Similar Problems and DFS:
    39. Combination Sum: self.DFS(arr[i:], tar - x)
    46. Permutations: self.DFS(arr[:i] + arr[i + 1:])
    78. Subsets: self.DFS(arr[i + 1:])

46. Permutations - <DFS, Backtracking>

48. Rotate Image - <2D-Array>

56. Merge Intervals - <Sort with lambda, Two Pointers>

75. Sort Colors - <Counting Sort, Two Pointers Partition>

78. Subsets - <DFS, Backtracking>

79. Word Search - <DFS, Backtracking>

215. Kth Largest Element in an Array - <Quick Sort, K-sized Heap, Quick Select>
"""
