# Leetcode 3137: Minimum Number of Operations to make Word K-Periodic
# https://leetcode.com/problems/minimum-number-of-operations-to-make-word-k-periodic/
# Solved on 23rd of June, 2025
from collections import Counter


class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        """
        Calculates the minimum number of operations to make a word k-periodic.

        A word is k-periodic if it can be formed by concatenating a string of length k
        some number of times. An operation consists of changing any character in the word.

        Args:
            word: The input string.
            k: The length of the periodic block.
        """
        n = len(word)
        numBlocks = n // k

        # Create a generator that yields each k-length block of the word.
        blocks = (word[i * k: (i + 1) * k] for i in range(numBlocks))

        # Count the occurrences of each unique block
        frequencies = Counter(blocks)

        # Find the frequency of the most common block.
        maxFrequency = 0
        if frequencies:
            maxFrequency = max(frequencies.values())

        # The number of operations is the total number of blocks.
        operations = numBlocks - maxFrequency

        return operations