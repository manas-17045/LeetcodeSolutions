# Leetcode 1815: Maximum Number of Groups Getting Fresh Donuts
# https://leetcode.com/problems/maximum-number-of-groups-getting-fresh-donuts/
# Solved on 21st of June, 2025
from functools import lru_cache


class Solution:
    def maxHappyGroups(self, batchSize: int, groups: list[int]) -> int:
        """
        Calculates the maximum number of happy groups that can be formed.

        A group is happy if its total size is a multiple of batchSize.
        We can combine groups to form happy groups.

        Args:
            batchSize: The size of each batch.
            groups: A list of integers representing the sizes of individual groups.
        Returns:
            The maximum number of happy groups.
        """
        # Count how many groups of each remainder we have
        cnt = [0] * batchSize
        for g in groups:
            cnt[g % batchSize] += 1

        # All groups with remainder 0 are automatically happy
        ans = cnt[0]

        # We'll only care about remainders 1...(batchSize - 1).
        rem_counts = tuple(cnt[1:])

        @lru_cache(None)
        def dfs(state: tuple, cur_mod: int) -> int:
            # state is a tuple of length (batchSize - 1), state[i - 1] = how many groups with remainder i remain
            best = 0
            # Try taking one group of each possible non-zero remainder
            for r in range(1, batchSize):
                if state[r - 1] > 0:
                    # Pick one group with remainder r
                    new_state = list(state)
                    new_state[r - 1] -= 1
                    new_state = tuple(new_state)

                    gain = 1 if cur_mod == 0 else 0
                    new_mod = (cur_mod + 1) % batchSize
                    best = max(best, (gain + dfs(new_state, new_mod)))

            return best

        # Start with no leftover (mod 0)
        ans += dfs(rem_counts, 0)
        return ans