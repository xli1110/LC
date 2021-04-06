"""
Tips:
    - dictionary
      d = {}
      d[key] = value
      dic.get(key, default)
      list(dic.keys())
    - set
      s = set()
      s.add(x)

1 - Hash Table for Checking Existence/Frequency

    Problems:
    1(two sum)
    36(valid sudoku)
    136, 217, 219(single number / duplicates) - hash/xor
    202(happy number) - store the cycle in a set
    242(anagram) - two dictionaries storing frequencies
    349, 350(intersection of arrays) - loop arr1 to construct the dic; loop arr2 for the res and modifying dic meanwhile

    Model:
    dic = {}
    for i, x in enumerate(arr):
        if x in dic:
            xxx
        else:
            xxx
        dic[x] = i

2 - Hash Table for Strings

    Problems:
    2(longest sub-string) - dp[i] denotes the maximum sub-string length ending at s[i]
    205(isomorphic strings)

3 - Others
    138(copy with random pointer) - see linked list
"""
