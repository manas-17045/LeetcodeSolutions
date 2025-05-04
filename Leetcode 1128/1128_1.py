# Leetcode 1128: Number of Equivalent Domino Pairs
# https://leetcode.com/problems/number-of-equivalent-domino-pairs/
from collections import defaultdict


class Solution:
    def numEquivDominoPairs(self, dominoes: list[list[int]]) -> int:
        pair_count = 0
        # Use defaultdict for slightly cleaner incrementing
        canonical_counts = defaultdict(int)

        for domino in dominoes:
            # Ensure a consistent order for the key (e.g., smallest first)
            # Create a tuple so it's hashable
            a, b = domino[0], domino[1]
            key = tuple(sorted(domino))
            # Alternative canonical key: key = (min(a, b), max(a, b))

            # Add the number of pairs this domino forms with previously seen ones
            pair_count += canonical_counts[key]

            # Increment the count for this canonical form
            canonical_counts[key] += 1

        return pair_count