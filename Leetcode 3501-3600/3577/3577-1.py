# Leetcode 3577: Count the Number of Computer Unlocking Permutations
# https://leetcode.com/problems/count-the-number-of-computer-unlocking-permutations/
# Solved on 9th of October, 2025
class Solution:
    def countPermutations(self, complexity: list[int]) -> int:
        """
        Counts the number of valid computer unlocking permutations.

        Args:
            complexity: A list of integers representing the complexity of each computer.
        Returns:
            The number of valid permutations modulo 10^9 + 7.
        """
        n = len(complexity)
        if n <= 1:
            return 1

        # Initial Validity Check
        minPrefixComplexity = complexity[0]
        for i in range(1, n):
            if complexity[i] <= minPrefixComplexity:
                return 0
            minPrefixComplexity = min(minPrefixComplexity, complexity[i])

        # Sort by complexity, then index
        computers = sorted([(complexity[i], i) for i in range(n)])

        # Root check
        if computers[0][1] != 0:
            return 0

        MOD = 10**9 + 7

        # Count permutations by groups
        permutations = 1
        numPlaced = 1
        i = 1

        while i < n:
            j = i
            while j < n and computers[j][0] == computers[i][0]:
                j += 1

            groupSize = j - i

            # Calculate P(numPlaced + groupSize - 1, groupSize)
            term = 1
            for k in range(groupSize):
                term = (term * (numPlaced + k)) % MOD

            permutations = (permutations * term) % MOD

            numPlaced += groupSize
            i = j

        return permutations