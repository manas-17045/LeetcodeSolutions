# Leetcode 3981: Count Distinct Ways to Form Target from Two Strings
# https://leetcode.com/problems/count-distinct-ways-to-form-target-from-two-strings/
# Solved on 1st of August, 2026
class Solution:
    def interleaveCharacters(self, word1: str, word2: str, target: str) -> int:
        """
        Determines the number of distinct ways to form the target string by interleaving
        characters from word1 and word2.
        
        Args:
            word1 (str): The first word.
            word2 (str): The second word.
            target (str): The target string to form.
        
        Returns:
            int: The number of distinct ways to form the target string.
        """
        modValue = 10**9 + 7
        len1 = len(word1)
        len2 = len(word2)
        targetLen = len(target)

        dp = [[[0] * 4 for _ in range(len2 + 1)] for _ in range(len1 + 1)]

        for i in range(len1 + 1):
            for j in range(len2 + 1):
                dp[i][j][3] = 1

        for t in range(targetLen - 1, -1, -1):
            charT = target[t]
            newDp = [[[0] * 4 for _ in range(len2 + 1)] for _ in range(len1 + 1)]

            for j in range(len2 + 1):
                sumW1 = 0
                for i in range(len1 - 1, -1, -1):
                    if word1[i] == charT:
                        sumW1 = (sumW1 +dp[i + 1][j][1]) % modValue
                    newDp[i][j][0] = sumW1
                    newDp[i][j][1] = sumW1

            for j in range(len2 + 1):
                sumW1 = 0
                for i in range(len1 - 1, -1, -1):
                    if word1[i] == charT:
                        sumW1 = (sumW1 + dp[i + 1][j][3]) % modValue
                    newDp[i][j][2] = sumW1
                    newDp[i][j][3] = sumW1

            for i in range(len1 + 1):
                sumW2 = 0
                for j in range(len2 - 1, -1, -1):
                    if word2[j] == charT:
                        sumW2 = (sumW2 + dp[i][j + 1][2]) % modValue
                    newDp[i][j][0] = (newDp[i][j][0] + sumW2) % modValue
                    newDp[i][j][2] = (newDp[i][j][2] + sumW2) % modValue

            for i in range(len1 + 1):
                sumW2 = 0
                for j in range(len2 - 1, -1, -1):
                    if word2[j] == charT:
                        sumW2 = (sumW2 + dp[i][j + 1][3]) % modValue
                    newDp[i][j][1] = (newDp[i][j][1] + sumW2) % modValue
                    newDp[i][j][3] = (newDp[i][j][3] + sumW2) % modValue

            dp = newDp

        return dp[0][0][0]