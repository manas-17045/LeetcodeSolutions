# Leetcode 2410: Maximum Matching of Players With Trainers
# https://leetcode.com/problems/maximum-matching-of-players-with-trainers/
# Solved on 13th of July, 2025
class Solution:
    def matchPlayersAndTrainers(self, players: list[int], trainers: list[int]) -> int:
        """
        Matches players with trainers such that each player is assigned to at most one trainer,
        and each trainer is assigned to at most one player. A player `p` can be matched
        with a trainer `t` only if `p <= t`. The goal is to maximize the number of successful matches.

        Args:
            players (list[int]): A list of integers representing the power of each player.
            trainers (list[int]): A list of integers representing the power of each trainer.

        Returns:
            int: The maximum number of successful matches.
        """
        players.sort()
        trainers.sort()

        i = j = matches = 0
        n, m = len(players), len(trainers)

        # Try to match each player in ascending order
        while i < n and j < m:
            if players[i] <= trainers[j]:
                matches += 1
                i += 1
                j += 1
            else:
                j += 1

        return matches