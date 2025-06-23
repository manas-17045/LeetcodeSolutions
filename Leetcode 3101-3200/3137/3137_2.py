# Leetcode 3137: Minimum Number of Operations to make Word K-Periodic
# https://leetcode.com/problems/minimum-number-of-operations-to-make-word-k-periodic/
# Solved on 23rd of June, 2025
class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        """
        Calculates the minimum operations to make a string k-periodic.

        A string is k-periodic if it can be formed by concatenating a string `t`
        of length `k` a certain number of times.

        The goal is to find the minimum number of operations (changing a character)
        to make the given `word` k-periodic.

        We achieve this by finding the most frequent block of length `k` in the
        `word` and then changing all other blocks to match it.
        """
        n = len(word)
        m = n // k
        # Count frequencies of each length-k block
        freq = {}
        for i in range(0, n, k):
            block = word[i:i + k]
            freq[block] = freq.get(block, 0) + 1

        # The best block to repeat is the one with maximum frequency.
        max_same = max(freq.values())
        # We need to overwrite every other block once
        return m - max_same