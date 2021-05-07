"""
Tips:
    1 - For arr string conversion, use string.join() as res.append("".join(path)).
    2 - Permutation/Combination usually needs to loop the whole array as for i, x in enumerate(arr).

1 - Backtracking

    Problems:
    17(combination + hash) - dic[digit] = [chars]; DFS(arr, path_len + 1)
    22(permutation + regulation) - DFS(n, num_left, num_right); if num_left < n; if num_right < num_left
    31(next permutation) - brute-force
    39(combination + target) - DFS(arr[i:], tar - x)
    46/47(permutation) - DFS(arr[:i] + arr[i + 1:])
    78(sub-set) - DFS(arr[i + 1:])
    79(2D array path search) - t = mat[i][j], mat[i][j] = None; DFS; mat[i][j] = t
"""
