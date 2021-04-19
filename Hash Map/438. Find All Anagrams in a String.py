class Solution:
    def generate_dic(self, s):
        d = {}
        for x in s:
            if x in d:
                d[x] += 1
            else:
                d[x] = 1
        return d

    def compare(self, s, p):
        """
        Similar to 242, compare two dictionaries + sliding window.
        Do not generate a new dictionary at each step.
        Change the current dictionary with the sliding window.
        O(MN)
        """
        dic = self.generate_dic(p)

        # init
        res = []
        temp = self.generate_dic(s[:len(p)])
        if temp == dic:
            res.append(0)

        # slide
        for start in range(1, len(s) - len(p) + 1):  # O(N)
            # delete
            x = s[start - 1]
            if temp[x] > 1:
                temp[x] -= 1
            else:
                temp.pop(x)

            # add
            y = s[start + len(p) - 1]
            if y in temp:
                temp[y] += 1
            else:
                temp[y] = 1

            # compare
            if temp == dic:  # O(M)
                res.append(start)

        return res

    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
            # raise Exception("Invalid String")

        return self.compare(s, p)
