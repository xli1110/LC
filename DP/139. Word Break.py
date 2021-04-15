class Solution:
    def wordBreak(self, s: str, wordDict: [str]) -> bool:
        """
        dp[i] represents whether s[:i + 1]'s break is in the word dictionary.
        """
        if not s:
            raise Exception("Empty String")
        if not wordDict:
            raise Exception("Empty Dictionary")

        word_set = set(wordDict)

        dp = [False] * len(s)

        for i in range(len(s)):
            for j in range(i, len(s)):
                # Note that when i == 0, we ONLY check whether s[:j + 1] is in the set.
                if i == 0:
                    if s[:j + 1] in word_set:
                        dp[j] = True
                else:
                    if dp[i - 1] and s[i:j + 1] in word_set:
                        # note dp[i - 1]
                        dp[j] = True
        return dp[-1]


if __name__ == "__main__":
    sol = Solution()

    s = "leetcode"
    arr = ["leet", "code"]

    print(sol.wordBreak(s, arr))
