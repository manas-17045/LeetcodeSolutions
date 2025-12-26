# Leetcode 3752: Lexicographically Smallest Negated Permutation that Sums to Target
# https://leetcode.com/problems/lexicographically-smallest-negated-permutation-that-sums-to-target/
# Solved on 26th of December, 2025
class Solution:
    def lexSmallestNegatedPerm(self, n: int, target: int) -> list[int]:
        """
        Finds the lexicographically smallest negated permutation of numbers from 1 to n that sums to target.

        Args:
            n: The upper bound of the numbers in the permutation (1 to n).
            target: The desired sum of the permutation.
        Returns:
            A list of integers representing the lexicographically smallest negated permutation, or an empty list if no such permutation exists.
        """
        totalSum = n * (n + 1) // 2
        diff = totalSum - target

        if diff < 0 or diff % 2 != 0:
            return []

        negSum = diff // 2
        isNegated = [False] * (n + 1)
        negatedNumbers = []

        for i in range(n, 0, -1):
            if negSum >= i:
                negSum -= i
                isNegated[i] = True
                negatedNumbers.append(-i)

        if negSum > 0:
            return []

        result = negatedNumbers

        for i in range(1, n + 1):
            if not isNegated[i]:
                result.append(i)

        return result