# Leetcode 3577: Count the Number of Computer Unlocking Permutations
# https://leetcode.com/problems/count-the-number-of-computer-unlocking-permutations/
# Solved on 10th of October, 2025
class Solution:
    def countPermutations(self, complexity: list[int]) -> int:
        """
        Calculates the number of valid permutations of a given complexity array.
        A permutation is valid if the first element is the unique global minimum.

        Args:
            complexity: A list of integers representing the complexity values.
        Returns:
            The number of valid permutations modulo 10^9 + 7.
        """
        MOD = 10**9 + 7
        n = len(complexity)
        # If complexity[0] is not the unique global minimum, impossible
        min_val = min(complexity)
        if complexity[0] != min_val or complexity.count(min_val) > 1:
            return 0

        # Otherwise, answer = (n - 1)! % MOD
        ans = 1
        for x in range(2, n):
            ans = (ans * x) % MOD
        return ans