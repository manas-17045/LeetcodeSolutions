# Leetcode 2225: Find Players With Zero or One Losses
# https://leetcode.com/problems/find-players-with-zero-or-one-losses/
# Solved on 10th of November, 2025
class Solution:
    def findWinners(self, matches: list[list[int]]) -> list[list[int]]:
        """
        Finds players who have not lost any matches and players who have lost exactly one match.

        Args:
            matches (list[list[int]]): A list of matches, where each match is [winner_player_id, loser_player_id].

        Returns:
            list[list[int]]: A list containing two sorted lists:
                             - The first list contains all players who have not lost any matches.
                             - The second list contains all players who have lost exactly one match.
        """
        lossCounts = {}

        for winner, loser in matches:
            lossCounts[winner] = lossCounts.get(winner, 0)
            lossCounts[loser] = lossCounts.get(loser, 0) + 1

        zeroLosses = []
        oneLoss = []

        for player, count in lossCounts.items():
            if count == 0:
                zeroLosses.append(player)
            elif count == 1:
                oneLoss.append(player)

        zeroLosses.sort()
        oneLoss.sort()

        return [zeroLosses, oneLoss]