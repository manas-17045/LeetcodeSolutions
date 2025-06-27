# Leetcode 2405: Optimal Partition of String
# https://leetcode.com/problems/optimal-partition-of-string/
# Solved on 27th of June, 2025
class Solution:
    def partitionString(self, s: str) -> int:
        """
        Given a string s, partition the string into one or more substrings such that the characters in each substring are unique.
        That is, no two characters in a substring are the same.

        Return the minimum number of substrings in such a partition.

        Note that each character should belong to exactly one substring in a partition.
        """
        # If s is empty, return 0
        if not s:
            return 0

        partitions = 1
        # 26-bit bitmask
        mask = 0

        for ch in s:
            bit = 1 << (ord(ch) - ord('a'))
            # If this character is already in the current substring, start a new one
            if mask & bit:
                partitions += 1
                mask = bit
            else:
                mask |= bit

        return partitions