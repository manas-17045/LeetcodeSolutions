# Leetcode 3193: Count the Number of Inversions
# https://leetcode.com/problems/count-the-number-of-inversions/
# Solved on 4th of October, 2025
class Solution:
    def numberOfPermutations(self, n: int, requirements: list[list[int]]) -> int:
        """
        Calculates the number of permutations of length `n` that satisfy the given inversion requirements.

        Args:
            n: The length of the permutation.
            requirements: A list of lists, where each inner list `[end, count]` specifies that the prefix of length
                          `end + 1` must have exactly `count` inversions.
        Returns:
            The number of valid permutations modulo 1,000,000,007.
        """
        mod = 1_000_000_007
        maxCount = 400

        requirementsMap = {end: count for end, count in requirements}

        dp = [0] * (maxCount + 1)
        dp[0] = 1

        if 0 in requirementsMap and requirementsMap[0] != 0:
            return 0

        for length in range(2, n + 1):
            newDp = [0] * (maxCount + 1)

            prefixSums = [0] * (maxCount + 1)
            prefixSums[0] = dp[0]
            for j in range(1, maxCount + 1):
                prefixSums[j] = (prefixSums[j - 1] + dp[j]) % mod

            for j in range(maxCount + 1):
                lowBound = j - (length - 1)

                sumValue = prefixSums[j]
                if lowBound > 0:
                    sumValue = (sumValue - prefixSums[lowBound - 1] + mod) % mod

                newDp[j] = sumValue

            dp = newDp

            endIndex = length - 1
            if endIndex in requirementsMap:
                requiredCount = requirementsMap[endIndex]
                for j in range(maxCount + 1):
                    if j != requiredCount:
                        dp[j] = 0

        return dp[requirementsMap[n - 1]]