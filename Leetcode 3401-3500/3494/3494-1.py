# Leetcode 3494: Find the Minimum Amount of Time to Brew Potions
# https://leetcode.com/problems/find-the-minimum-amount-of-time-to-brew-potions/
# Solved on 9th of October, 2025
class Solution:
    def minTime(self, skill: list[int], mana: list[int]) -> int:
        """
        Calculates the minimum time to brew all potions.

        Args:
            skill: A list of integers representing the skill level of each alchemist.
            mana: A list of integers representing the mana cost of each potion.
        Returns:
            The minimum total time required to brew all potions.
        """
        n = len(skill)
        m = len(mana)

        if n == 0 or m == 0:
            return 0

        prev_finish = [0] * n

        for j in range(m):
            p = [skill[i] * mana[j] for i in range(n)]
            prefix = [0] * (n + 1)

            for i in range(n):
                prefix[i + 1] = prefix[i] + p[i]

            S = float('-inf')
            for k in range(n):
                S = max(S, prev_finish[k] - prefix[k])

            curr_finish = [0] * n

            for k in range(n):
                curr_finish[k] = S + prefix[k + 1]

            prev_finish = curr_finish

        return prev_finish[n - 1]