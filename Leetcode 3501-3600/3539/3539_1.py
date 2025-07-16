# Leetcode 3539: Find Sum of Array Product of Magical Sequences
# https://leetcode.com/problems/find-sum-of-array-product-of-magical-sequences/
# Solved on 16th of July, 2025
class Solution:
    def magicalSum(self, m: int, k: int, nums: list[int]) -> int:
        """
        Calculates the sum of array products of magical sequences.

        A magical sequence is an array `a` of length `m` such that each element `a[j]`
        is chosen from `nums` (with replacement), and the sum of elements `sum(a)`
        has a popcount (number of set bits in its binary representation) equal to `k`.

        The problem asks for the sum of products `product(a)` for all such magical sequences `a`.

        Args:
            m: The length of the magical sequences.
            k: The required popcount of the sum of elements in a magical sequence.
            nums: A list of integers from which elements of the magical sequence can be chosen.

        Returns:
            The sum of array products of magical sequences, modulo 10^9 + 7.
        """
        mod = 10**9 + 7
        n = len(nums)

        fact = [1] * (m + 1)
        invFact = [1] * (m + 1)
        for i in range(1, (m + 1)):
            fact[i] = (fact[i - 1] * i) % mod

        invFact[m] = pow(fact[m], (mod - 2), mod)
        for i in range(m - 1, -1, -1):
            invFact[i] = (invFact[i + 1] * (i + 1)) % mod

        numPowers = [[0] * (m + 1) for _ in range(n)]
        for i in range(n):
            numPowers[i][0] = 1
            for j in range(1, m + 1):
                numPowers[i][j] = (numPowers[i][j - 1] * nums[i]) % mod

        popCount = [bin(i).count('1') for i in range(m + 1)]

        dp = [[[0] * (k + 1) for _ in range(m + 1)] for _ in range(m + 1)]
        dp[0][0][0] = 1

        for i in range(n):
            newDp = [[[0] * (k + 1) for _ in range(m + 1)] for _ in range(m + 1)]
            for countUsed in range(m + 1):
                for carryIn in range(m + 1):
                    for bitsCount in range(k + 1):
                        if dp[countUsed][carryIn][bitsCount] == 0:
                            continue

                        currentVal = dp[countUsed][carryIn][bitsCount]

                        for countForNumI in range(m - countUsed + 1):
                            newCountUsed = countUsed + countForNumI

                            totalValAtPos = countForNumI + carryIn
                            bit = totalValAtPos % 2
                            newCarryOut = totalValAtPos // 2

                            newBitsCount = bitsCount + bit

                            if newBitsCount <= k:
                                term = (numPowers[i][countForNumI] * invFact[countForNumI]) % mod
                                increment = (currentVal * term) % mod
                                newDp[newCountUsed][newCarryOut][newBitsCount] = (newDp[newCountUsed][newCarryOut][newBitsCount] + increment) % mod
            dp = newDp

        totalSumCoeffs = 0
        finalDpState = dp[m]
        for finalCarry in range(m + 1):
            for bitsCount in range(k + 1):
                if finalDpState[finalCarry][bitsCount] == 0:
                    continue

                if bitsCount + popCount[finalCarry] == 0:
                    totalSumCoeffs = (totalSumCoeffs + finalDpState[finalCarry][bitsCount]) % mod

        return (totalSumCoeffs * fact[m]) % mod