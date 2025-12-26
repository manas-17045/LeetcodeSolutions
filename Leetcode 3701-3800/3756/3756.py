# Leetcode 3756: Concatenate Non-Zero Digits and Multiply by Sum II
# https://leetcode.com/problems/concatenate-non-zero-digits-and-multiply-by-sum-ii/
# Solved on 26th of December, 2025
class Solution:
    def sumAndMultiply(self, s: str, queries: list[list[int]]) -> list[int]:
        """
        Calculates the product of the concatenated non-zero digits and the sum of digits for given ranges.

        Args:
            s (str): The input string of digits.
            queries (list[list[int]]): A list of queries, where each query is [l, r] representing a range.
        Returns:
            list[int]: A list of integers, where each element is the result for the corresponding query.
        """
        mod = 10 ** 9 + 7
        n = len(s)

        powers = [1] * (n + 1)
        invPowers = [1] * (n + 1)
        inv10 = pow(10, mod - 2, mod)

        currPower = 1
        currInv = 1
        for i in range(1, n + 1):
            currPower = (currPower * 10) % mod
            powers[i] = currPower
            currInv = (currInv * inv10) % mod
            invPowers[i] = currInv

        nonZeroCounts = [0] * (n + 1)
        digitSums = [0] * (n + 1)
        weightedSums = [0] * (n + 1)

        runningCount = 0
        runningSum = 0
        runningWeightedSum = 0

        for i in range(n):
            digit = int(s[i])
            if digit != 0:
                runningCount += 1
                runningSum += digit
                term = (digit * invPowers[runningCount]) % mod
                runningWeightedSum = (runningWeightedSum + term) % mod

            nonZeroCounts[i + 1] = runningCount
            digitSums[i + 1] = runningSum
            weightedSums[i + 1] = runningWeightedSum

        results = []
        for l, r in queries:
            count = nonZeroCounts[r + 1] - nonZeroCounts[l]
            if count == 0:
                results.append(0)
                continue

            rangeSum = digitSums[r + 1] - digitSums[l]

            weightedDiff = (weightedSums[r + 1] - weightedSums[l]) % mod
            reconstructedX = (weightedDiff * powers[nonZeroCounts[r + 1]]) % mod

            finalRes = (reconstructedX * rangeSum) % mod
            results.append(finalRes)

        return results