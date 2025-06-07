# Leetcode 3333: Find the Original Typed String II
# https://leetcode.com/problems/find-the-original-typed-string-ii/
# Solved on 7th of June, 2025

class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        """
        Calculates the number of possible original strings that could have been typed
        to produce the given `word` after applying a specific typing process.

        Args:
            word: The typed string.
            k: The maximum number of groups of consecutive identical characters allowed in the original string.

        Returns:
            The number of possible original strings modulo 10^9 + 7.
        """
        MOD = 1_000_000_007

        if not word:
            return 0

        groupLengths = []
        if len(word) > 0:
            count = 1
            for i in range(1, len(word)):
                if word[i] == word[i - 1]:
                    count += 1
                else:
                    groupLengths.append(count)
                    count = 1
            groupLengths.append(count)

        m = len(groupLengths)

        totalStrings = 1
        for groupLen in groupLengths:
            totalStrings = (totalStrings * groupLen) % MOD

        if m >= k:
            return totalStrings

        dp = [0] * k
        dp[0] = 1

        for groupLen in groupLengths:
            prefixSum = [0] * k
            currentSum = 0
            for i in range(k):
                currentSum = (currentSum + dp[i]) % MOD
                prefixSum[i] = currentSum

            newDp = [0] * k
            for j in range(1, k):
                upperBound = prefixSum[j - i]
                lowerBound = prefixSum[j - groupLen - 1] if j - groupLen - 1 >= 0 else 0
                newDp[j] = (upperBound - lowerBound + MOD) % MOD
            dp = newDp

        badStrings = 0
        for count in dp:
            badStrings = (badStrings + count) % MOD

        return (totalStrings - badStrings + MOD) % MOD