# Leetcode 1434: Number of Ways to Wear Different Hats to Each Other
# https://leetcode.com/problems/number-of-ways-to-wear-different-hats-to-each-other/
# Solved on 10th of August, 2025
class Solution:
    def numberWays(self, hats: list[list[int]]) -> int:
        """
        Calculates the number of ways to assign hats to people such that each person gets a hat they like,
        and no two people share the same hat.

        Args:
            hats: A list of lists, where hats[i] is a list of integers representing the hats that person i likes.
        Returns:
            The number of ways to assign hats, modulo 10^9 + 7.
        """
        MOD = 10**9 + 7
        n = len(hats)
        if n == 0:
            return 1

        hat_people = [[] for _ in range(41)]
        for persson, hat_list in enumerate(hats):
            for h in hat_list:
                hat_people[h].append(persson)

        full = (1 << n) - 1
        dp = [0] * (1 << n)
        dp[0] = 1

        # Process hats one by one
        for h in range(1, 41):
            people = hat_people[h]
            if not people:
                continue
            dp2 = dp[:]
            # For every assignment mask, try assigning this hat to one unassigned person who likes it
            for mask in range(1 << n):
                ways = dp[mask]
                if ways == 0:
                    continue
                for p in people:
                    # If person p is not assigned in mask
                    if not (mask & p) & 1:
                        new_mask = mask | (1 << p)
                        dp2[new_mask] = (dp2[new_mask] + ways) % MOD
            dp = dp2

        return dp[full]