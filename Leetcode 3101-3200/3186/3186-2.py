# Leetcode 3186: Maximum Total Damage With Spell Casting
# https://leetcode.com/problems/maximum-total-damage-with-spell-casting/
# Solved on 8th of October, 2025
from collections import Counter


class Solution:
    def maximumTotalDamage(self, power: list[int]) -> int:
        """
        Calculates the maximum total damage that can be dealt by selecting a subset of powers.

        :param power: A list of integers representing the power values of available attacks.
        :return: The maximum total damage that can be dealt.
        """
        # Count frequency of each power value
        freq = Counter(power)

        # Get unique powers and sort them
        unique_powers = sorted(freq.keys())
        n = len(unique_powers)

        if n == 0:
            return 0
        if n == 1:
            return unique_powers[0] * freq[unique_powers[0]]

        # DP array where dp[i] = max damage using powers from index 0 to i
        dp = [0] * n

        # Base case: first power
        dp[0] = unique_powers[0] * freq[unique_powers[0]]

        # For second power, check if it conflicts with first
        if unique_powers[1] - unique_powers[0] <= 2:
            # They conflict, take the maximum
            dp[1] = max(dp[0], unique_powers[1] * freq[unique_powers[1]])
        else:
            # No conflict, take both
            dp[1] = dp[0] + unique_powers[1] * freq[unique_powers[1]]

        # Fill the DP table
        for i in range(2, n):
            current_power = unique_powers[i]
            current_damage = current_power * freq[current_power]

            # Skip current power
            skip = dp[i - 1]

            # Take current power
            # Find the last index j where unique_powers[j] < current_power - 2
            take = current_damage
            j = i - 1
            while j >= 0 and unique_powers[j] > current_power - 3:
                j -= 1

            if j >= 0:
                take += dp[j]

            dp[i] = max(skip, take)

        return dp[n - 1]