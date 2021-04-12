import string


class Solution:
    def freq_code(self, strs):
        """
        1 - Generate a freq dictionary of the string.
        2 - Code the freq dictionary.
        3 - Hash the code as dic[code] = [s1, s2, ...]
        4 - return list(dic.values())

        This method sucks at step2, since different anagrams may map the same code.
        s1 = "bdddddddddd", freq1 = 01010..., a:0, b:1, c:0, d:10
        s2 = "bbbbbbbbbbc", freq2 = 01010..., a:0, b:10, c:0
        dic[0101000000...] = ["bdddddddddd", "bbbbbbbbbbc"] => WRONG
        """
        dic = {}
        letters = string.ascii_lowercase

        for s in strs:
            # generate the freq dic
            temp = {char: 0 for char in letters}
            for char in s:
                temp[char] += 1

            # code the freq
            freq = ""
            for key in letters:
                freq += str(temp[key])

            # build k-v pairs, like freq : [s1, s2, s3, ...]
            if freq in dic:
                dic[freq].append(s)
            else:
                dic[freq] = [s]

        return list(dic.values())

    def freq_code2(self, strs):
        """
        1 - Calculate the freq code as an array, and transform it into a tuple.
        2 - Hash the code as dic[code] = [s1, s2, ...]
        4 - return list(dic.values())
        """
        dic = {}

        for s in strs:
            freq = [0] * 26
            for char in s:
                freq[ord(char) - 97] += 1

            tu = tuple(freq)

            if tu in dic:
                dic[tu].append(s)
            else:
                dic[tu] = [s]

        return list(dic.values())

    def groupAnagrams(self, strs: [str]) -> [[str]]:
        if not strs:
            raise Exception("Empty Array")

        # return self.freq_code(strs)
        return self.freq_code2(strs)


if __name__ == "__main__":
    sol = Solution()
    strs = ["bdddddddddd", "bbbbbbbbbbc"]
    res = sol.groupAnagrams(strs)
    print(res)
