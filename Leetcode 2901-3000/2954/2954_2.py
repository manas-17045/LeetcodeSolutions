# Leetcode 2954: Count the Number of Infection Sequences
# https://leetcode.com/problems/count-the-number-of-infection-sequences/
# Solved on 14th of June, 2025

class Solution:
    def numberOfSequence(self, n: int, sick: list[int]) -> int:
        """
        Calculates the number of ways to arrange uninfected people given the positions of sick people.

        The problem can be broken down into two parts:
        1. The number of ways to arrange the uninfected people within the segments created by the sick people.
        2. The number of ways to arrange the uninfected people between these segments.

        Args:
            n: The total number of people.
            sick: A list of integers representing the indices of the sick people.

        Returns:
            The number of possible arrangements of uninfected people modulo 10^9 + 7.
        """
        mod = 10**9 + 7

        factorials = [1] * (n + 1)
        inverseFactorials = [1] * (n + 1)
        for i in range(1, (n + 1)):
            factorials[i] = (factorials[i - 1] * i) % mod

        inverseFactorials[n] = pow(factorials[n], (mod - 2), mod)
        for i in range((n - 1), -1, -1):
            inverseFactorials[i] = (inverseFactorials[i + 1] * (i + 1)) % mod

        segmentSizes = []

        firstSegmentSize = sick[0]
        if firstSegmentSize > 0:
            segmentSizes.append(firstSegmentSize)

        internalPermutations = 1
        for i in range(len(sick) - 1):
            middleSegmentSize = sick[i + 1] - sick[i] - 1
            if middleSegmentSize > 0:
                segmentSizes.append(middleSegmentSize)
                powerOfTwo = pow(2, (middleSegmentSize - 1), mod)
                internalPermutations = (internalPermutations * powerOfTwo) % mod

        lastSegmentSize = n - 1 - sick[-1]
        if lastSegmentSize > 0:
            segmentSizes.append(lastSegmentSize)

        totalUninfected = n - len(sick)

        interLeavingWays = factorials[totalUninfected]
        for size in segmentSizes:
            interLeavingWays = (interLeavingWays * inverseFactorials[size]) % mod

        result = (interLeavingWays * internalPermutations) % mod

        return result