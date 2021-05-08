"""
Tips:
    1 - dictionary
        d = {}
        d[key] = value
        dic.get(key, default)
        dic.pop(key)
        list(dic.keys())
        list(dic.values())
    2 - set
        s = set()
        s.add(x)



1 - Hash Table for Checking Existence/Frequency

    Problems:
    1(two sum)
    36(valid sudoku)
    49(anagrams) - ord()/chr(); calculate the freq arr; hash the TUPLE(arr) as dic[tu] = [s1, s2, ...]
    136, 217, 219(single number / duplicates) - hash/xor
    169(majority)
    202(happy number) - store the cycle in a set
    205(isomorphic strings)
    242(valid anagram) - two dictionaries storing frequencies
    349, 350(intersection of arrays) - loop arr1: d[x] += 1; loop arr2: res.append(x), d[x] -= 1
    438(find anagrams) - 242 compare dictionaries + sliding window
    448(disappeared numbers) - loop one: hash construction; loop two: check disappearance

    Model:
    dic = {}
    for i, x in enumerate(arr):
        if x in dic:
            xxx
        else:
            xxx
        dic[x] = i
"""
