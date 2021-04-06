class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        loop:
            if dic consists of char:
                # use the smaller to iterate
                if i - dic[char] <= dp[i - 1]:
                    dp[i] = i - dic[char]
                else:
                    dp[i] = dp[i - 1] + 1
            else:
                dp[i] = dp[i - 1] + 1

            dic[char] = i
        """
        if not s:
            return 0

        dic = {s[0]: 0}  # dic[char] = index, where index denotes the char's last appearance position.
        dp = [1] * len(s)  # dp[i] stores the maximal sub-string length ending at s[j].

        for i in range(1, len(s)):
            char = s[i]
            if char in dic:
                if i - dic[char] <= dp[i - 1]:
                    # Note the LEQ here.
                    # BXXXAXXBA, dp[j - 1] = 7, j - index = 4, dp[j] = 4 (XXBA)
                    dp[i] = i - dic[char]
                else:
                    # AXXXXXBXXXBA, dp[j - 1] = 4, j - index = 11, dp[j] = 5 (XXXBA)
                    dp[i] = dp[i - 1] + 1
            else:
                # XXXXXBA, dp[j - 1] = 6, dp[j] = 7 (XXXXXBA)
                dp[i] = dp[i - 1] + 1
            dic[char] = i
        return max(dp)
