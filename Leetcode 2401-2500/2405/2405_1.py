# Leetcode 2405: Optimal Partition of String
# https://leetcode.com/problems/optimal-partition-of-string/
# Solved on 27th of June, 2025
class Solution:
    def partitionString(self, s: str) -> int:
        """
        Partitions a string into the minimum number of substrings such that
        each character appears at most once in each substring.

        Args:
            s: The input string.
        Returns:
            The minimum number of substrings.
        """
        count = 1
        currentSet = set()

        for char in s:
            if char in currentSet:
                count += 1
                currentSet = {char}
            else:
                currentSet.add(char)

        return count