# Leetcode 2660: Determine the Winner of a Bowling Game
# https://leetcode.com/problems/determine-the-winner-of-a-bowling-game/
# Solved on 5th of March, 2026
class Solution:
    def isWinner(self, player1: list[int], player2: list[int]) -> int:
        """
        Determines the winner of a bowling game based on specific scoring rules.

        :param player1: List of integers representing pins hit by player 1 in each turn.
        :param player2: List of integers representing pins hit by player 2 in each turn.
        :return: 1 if player 1 wins, 2 if player 2 wins, and 0 if it's a draw.
        """
        def calculateScore(playerScores):

            totalScore = 0
            for i in range(len(playerScores)):
                if (i > 0 and playerScores[i - 1] == 10) or (i > 1 and playerScores[i - 2] == 10):
                    totalScore += 2 * playerScores[i]
                else:
                    totalScore += playerScores[i]

            return totalScore

        playerOneScore = calculateScore(player1)
        playerTwoScore = calculateScore(player2)

        return 1 if playerOneScore > playerTwoScore else 2 if playerTwoScore > playerOneScore else 0