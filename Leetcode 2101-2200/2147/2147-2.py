# Leetcode 2147: Number of Ways to Divide a Long Corridor
# https://leetcode.com/problems/number-of-ways-to-divide-a-long-corridor/
# Solved on 6th of September, 2025
class Solution:
    def numberOfWays(self, corridor: str) -> int:
        """
        Calculates the number of ways to divide a corridor into sections, where each section contains exactly two plants.

        Args:
            corridor (str): A string representing the corridor, consisting of 'S' (plant) and 'P' (divider).
        Returns:
            int: The number of ways to divide the corridor, modulo 10^9 + 7.
        """
        MOD = 10 ** 9 + 7

        total_seats = corridor.count('S')
        if total_seats == 0 or total_seats % 2 == 1:
            return 0

        ways = 1
        seats_in_current_pair = 0
        prev_pair_second = -1  # index of the second seat of the previous completed pair
        have_prev_pair = False

        for i, ch in enumerate(corridor):
            if ch != 'S':
                continue

            seats_in_current_pair += 1
            if seats_in_current_pair == 1:
                # First seat of a new pair
                if have_prev_pair:
                    gap = i - prev_pair_second
                    ways = (ways * gap) % MOD
            else:
                # Second seat completes the current pair
                prev_pair_second = i
                have_prev_pair = True
                seats_in_current_pair = 0

        return ways