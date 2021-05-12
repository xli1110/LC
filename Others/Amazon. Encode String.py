"""
Encode String: Input -> Output:

aaaab -> 4xab,
aabb -> 2xa2xb,
abcccc -> ab3xc,
aa -> a != 2xa
x -> x != x
"""


def encode(s):
    if not s:
        raise Exception("Empty String")

    res = ""

    ch = s[0]
    num = 1

    flag_unique = True

    for i in range(1, len(s)):
        if s[i] == ch:
            num += 1
        else:
            res += (str(num) + "x" + ch) if num != 1 else ch
            ch = s[i]
            num = 1
            flag_unique = False

    # add the last part
    res += (str(num) + "x" + ch) if num != 1 else ch

    # check unique
    if flag_unique:
        res = (ch + " != ") + res

    return res


if __name__ == "__main__":
    """
    aaaab -> 4xab,
    aabb -> 2xa2xb,
    abcccc -> ab4xc,
    aa -> a != 2xa
    x -> x != x
    """
    print(encode("aaaab"))
    print(encode("aabb"))
    print(encode("abcccc"))
    print(encode("aa"))
    print(encode("x"))
    print(encode("abab"))
