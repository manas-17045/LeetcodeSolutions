# Leetcode 1639: Number of Ways to Form a Target String Given a Dictionary
# https://leetcode.com/problems/number-of-ways-to-form-a-target-string-given-a-dictionary/
# Resolved on 25th of August, 2025
class Solution:
    def numWays(self, words: list[str], target: str) -> int:
        """
        Calculates the number of ways to form the target string using characters from the given words.

        Args:
            words (list[str]): A list of strings, all of the same length.
            target (str): The target string to form.
        Returns:
            int: The number of ways to form the target string, modulo 10^9 + 7.
        """
        targetLen = len(target)
        wordLen = len(words[0])
        mod = 10 ** 9 + 7

        counts = [[0] * 26 for _ in range(wordLen)]
        for j in range(wordLen):
            for word in words:
                counts[j][ord(word[j]) - ord('a')] += 1

        dp = [1] * (wordLen + 1)

        for i in range(1, targetLen + 1):
            nextDp = [0] * (wordLen + 1)
            charIndex = ord(target[i - 1]) - ord('a')

            for j in range(1, wordLen + 1):
                countOfChar = counts[j - 1][charIndex]

                waysWithoutColumn = nextDp[j - 1]
                waysWithColumn = (dp[j - 1] * countOfChar)

                nextDp[j] = (waysWithoutColumn + waysWithColumn) % mod

            dp = nextDp

        return dp[wordLen]