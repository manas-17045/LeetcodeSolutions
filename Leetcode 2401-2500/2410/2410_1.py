# Leetcode 2410: Maximum Matching of Players With Trainers
# https://leetcode.com/problems/maximum-matching-of-players-with-trainers/
# Solved on 13th of July, 2025
class Solution:
    def matchPlayersAndTrainers(self, players: list[int], trainers: list[int]) -> int:
        """
        Matches players with trainers based on their abilities.
        :param players: List of player abilities.
        :param trainers: List of trainer abilities.
        :return: Maximum number of successful matches.
        """
        players.sort()
        trainers.sort()

        playerIndex = 0
        trainerIndex = 0
        matchCount = 0

        while playerIndex < len(players) and trainerIndex < len(trainers):
            if players[playerIndex] <= trainers[trainerIndex]:
                matchCount += 1
                playerIndex += 1
                trainerIndex += 1
            else:
                trainerIndex += 1

        return matchCount