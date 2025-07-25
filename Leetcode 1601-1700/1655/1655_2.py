# Leetcode 1655: Distribute Repeating Integers
# https://leetcode.com/problems/distribute-repeating-integers/
# Solved on 25th of July, 2025
import collections


class Solution:
    def canDistribute(self, nums: list[int], quantity: list[int]) -> bool:
        """
        Determines if it's possible to distribute items from `nums` to satisfy all customer `quantity` demands.
        :param nums: A list of integers representing the available items.
        :param quantity: A list of integers representing the demand of each customer.
        :return: True if all customers' demands can be satisfied, False otherwise.
        """

        # Count how many copies we have of each distinct integer
        freq = list(collections.Counter(nums).values())
        # Sort descending to try large capacities first (early pruning)
        freq.sort(reverse=True)

        m = len(quantity)
        full_mask = (1 << m) - 1

        # Precompute total demand for every subset mask of customers
        sum_demand = [0] * (1 << m)
        for mask in range(1, 1 << m):
            # Take least significant set bit
            lsb = mask & -mask
            idx = (lsb.bit_length() - 1)
            prev = mask ^ lsb
            sum_demand[mask] = sum_demand[prev] + quantity[idx]

        # dp[mask] = True if we can satisfy exactly the customers in 'mask' so far
        dp = [False] * (1 << m)
        dp[0] = True

        # Try each bucket one by one
        for cap in freq:
            # If we've already satisfied everyone, stop early
            if dp[full_mask]:
                return True

            # Gather all subset‑masks we could serve with this bucket alone
            valid = [mask for mask in range(1, 1 << m)
                     if sum_demand[mask] <= cap]

            # next_dp accumulates states reachable after using this bucket
            next_dp = dp[:]

            # From every already-reachable mask, try to add any non-overlapping valid subset
            for mask in range(1 << m):
                if not dp[mask]:
                    continue
                free = full_mask ^ mask
                # Try giving this bucket to any subset of the yet-unserved customers
                for sub in valid:
                    if sub & mask:
                        # That subset overlaps customers we've already served
                        continue
                    new_mask = mask | sub
                    if not next_dp[new_mask]:
                        next_dp[new_mask] = True
            dp = next_dp

        return dp[full_mask]