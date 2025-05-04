# Leetcode 1128: Number of Equivalent Domino Pairs
# https://leetcode.com/problems/number-of-equivalent-domino-pairs/

class Solution:
    def numEquivDominoPairs(self, dominoes: list[list[int]]) -> int:
        # Use a dictionary to count occurrences of each domino pattern
        domino_counts = {}

        # Count occurrences of each normalized domino
        for a, b in dominoes:
            # Normalize the domino by sorting its values
            # This ensures [a, b] and [b,a] are treated as the same
            key = tuple(sorted([a,b]))
            domino_counts[key] = domino_counts.get(key, 0) + 1

        # Calculate the total number of pairs
        total_pairs = 0
        for count in domino_counts.values():
            # If we have n identical dominoes, we can form n*(n-1)/2 pairs
            if count > 1:
                total_pairs += count * (count - 1) // 2

        return total_pairs