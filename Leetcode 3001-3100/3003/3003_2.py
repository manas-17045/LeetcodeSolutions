# Leetcode 3003: Maximize the Number of Partitions After Operations
# https://leetcode.com/problems/maximize-the-number-of-partitions-after-operations/
# Solved on 2nd of July, 2025
from functools import lru_cache


class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        """
        Calculates the maximum number of partitions possible in a string `s`
        such that each partition contains at most `k` distinct characters.
        One operation is allowed: changing exactly one character in the entire string.

        Args:
            s (str): The input string.
            k (int): The maximum number of distinct characters allowed in a partition.

        Returns:
            int: The maximum number of partitions.
        """
        n = len(s)

        @lru_cache(None)
        def dfs(i:int, can_change: bool, mask: int) -> int:
            # Base case: Reached the end of the string
            if i == n:
                return 0

            res = 0
            # Option 1: Keep s[i]
            bit = 1 << (ord(s[i]) - ord('a'))
            res = max(res, _handle(i, can_change, mask, bit))

            # Option 2: Change s[i] to any other letter
            if can_change:
                for c in range(26):
                    if bit & (1 << c):
                        continue
                    res = max(res, _handle(i, False, mask, 1 << c))

            return res

        def _handle(i: int, next_can_change: bool, mask: int, new_bit: int) -> int:
            new_mask = mask | new_bit
            # If more than k_distinct, cut partition here
            if new_mask.bit_count() > k:
                # Start new partition with only this character
                return 1 + dfs((i + 1), next_can_change, new_bit)
            # Otherwise, continue extending the current partition
            return dfs((i + 1), next_can_change, new_mask)

        return dfs(0, True, 0) + 1