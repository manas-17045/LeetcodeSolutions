# Leetcode 1815: Maximum Number of Groups Getting Fresh Donuts
# https://leetcode.com/problems/maximum-number-of-groups-getting-fresh-donuts/
# Solved on 21st of June, 2025
from functools import lru_cache


class Solution:
    def maxHappyGroups(self, batchSize: int, groups: list[int]) -> int:
        """
        Calculates the maximum number of happy groups that can be formed from a list of groups,
        given a specific batch size. A group is happy if the sum of its members' remainders
        when divided by batchSize is 0.

        Args:
            batchSize (int): The size of each batch.
            groups (list[int]): A list of integers representing the sizes of individual groups.
        Returns:
            int: The maximum number of happy groups.
        """
        counts = [0] * batchSize
        for g_val in groups:
            counts[g_val % batchSize] += 1

        initial_happy_groups = counts[0]

        for j in range(1, batchSize):
            # Pair (batchSize - j, j) already processed when iterating smaller value
            if j > (batchSize - j):
                continue

            # Standard pair (j, (batchSize - j))
            if j < (batchSize - j):
                num_pairs = min(counts[j], counts[batchSize - j])
                initial_happy_groups += num_pairs
                counts[j] -= num_pairs
                counts[batchSize - j] -= num_pairs
            elif j * 2 == batchSize:
                num_mid_pairs = counts[j] // 2
                initial_happy_groups += num_mid_pairs
                counts[j] %= 2

        # Prepare dp_counts_tuple for non-zero remainders (1, 2, ..., (batchSize - 1))
        dp_counts_list = []
        for i in range(1, batchSize):
            dp_counts_list.append(counts[i])
        initial_dp_counts_tuple = tuple(dp_counts_list)

        @lru_cache(None)
        def dfs(current_counts_tuple, current_remainder):
            state_sum = sum(current_counts_tuple)
            if state_sum == 0:
                return 0

            max_additional_happy = 0

            for i in range(batchSize - 1):
                if current_counts_tuple[i] > 0:
                    group_rem_val = i + 1

                    new_counts_list = list(current_counts_tuple)
                    new_counts_list[i] -= 1
                    new_counts_tuple = tuple(new_counts_list)

                    current_group_is_happy = 1 if current_remainder == 0 else 0

                    recursive_result = dfs(new_counts_tuple, (current_remainder + group_rem_val) % batchSize)

                    current_path_happy_count = current_group_is_happy + recursive_result
                    if current_path_happy_count > max_additional_happy:
                        max_additional_happy = current_path_happy_count

            return max_additional_happy

        dp_result = dfs(initial_dp_counts_tuple, 0)

        return initial_happy_groups + dp_result