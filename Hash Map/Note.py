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
    169(majority)
    202(happy number) - store the cycle in a set
    242(anagram) - two dictionaries storing frequencies
    349, 350(intersection of arrays) - loop arr1: d[x] += 1; loop arr2: res.append(x), d[x] -= 1
    448(disappeared numbers) - loop one: hash construction; loop two: check disappearance

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
    205(isomorphic strings)

3 - Others
    138(copy with random pointer) - see linked list
"""
