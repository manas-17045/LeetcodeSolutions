# Leetcode 3186: Maximum Total Damage With Spell Casting
# https://leetcode.com/problems/maximum-total-damage-with-spell-casting/
# Solved on 8th of October, 2025
from collections import Counter


class Solution:
    def maximumTotalDamage(self, power: list[int]) -> int:
        """
        Calculates the maximum total damage that can be dealt by casting spells.

        Args:
            power: A list of integers representing the damage values of available spells.
        Returns:
            The maximum total damage that can be dealt.
        """
        powerCounts = Counter(power)
        uniquePowers = sorted(powerCounts.keys())

        n = len(uniquePowers)
        dp = [0] * n

        j = 0
        for i in range(n):
            currentPower = uniquePowers[i]

            while uniquePowers[j] < currentPower - 2:
                j += 1

            damageIncluded = currentPower * powerCounts[currentPower]
            if j > 0:
                damageIncluded += dp[j - 1]

            damageSkipped = dp[i - 1] if i > 0 else 0

            dp[i] = max(damageIncluded, damageSkipped)

        return dp[-1] if n > 0 else 0