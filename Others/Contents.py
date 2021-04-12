"""
----Easy----

283. Move Zeroes - <Array, Partition>

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

39. Combination Sum - <DFS, Backtracking, Combination / Permutation + Distinct>
    Notes:
    1 - Try to understand the DFS.

46. Permutations - <DFS, Backtracking>

48. Rotate Image - <2D-Array>


215. Kth Largest Element in an Array - <Quick Sort, Heap, Quick Select>
"""
