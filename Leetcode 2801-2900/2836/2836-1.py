# Leetcode 2836: Maximize Value of Function in a Ball Passing Game
# https://leetcode.com/problems/maximize-value-of-function-in-a-ball-passing-game/
# Solved on 31st of August, 2025
class Solution:
    def getMaxFunctionValue(self, receiver: list[int], k: int) -> int:
        """
        Calculates the maximum possible score achievable in a ball passing game.

        Args:
            receiver (list[int]): A list where receiver[i] is the player who receives the ball from player i.
            k (int): The number of passes.
        Returns:
            int: The maximum possible score.
        """
        numPlayers = len(receiver)
        maxLogK = k.bit_length()

        jumpTo = [[0] * numPlayers for _ in range(maxLogK)]
        jumpScore = [[0] * numPlayers for _ in range(maxLogK)]

        for i in range(numPlayers):
            jumpTo[0][i] = receiver[i]
            jumpScore[0][i] = receiver[i]

        for j in range(1, maxLogK):
            for i in range(numPlayers):
                prevPlayer = jumpTo[j - 1][i]
                jumpTo[j][i] = jumpTo[j - 1][prevPlayer]
                jumpScore[j][i] = jumpScore[j - 1][i] + jumpScore[j - 1][prevPlayer]

        maxScore = 0
        for startNode in range(numPlayers):
            currentScore = startNode
            currentNode = startNode

            remainingPasses = k
            for bit in range(maxLogK):
                if (remainingPasses >> bit) & 1:
                    currentScore += jumpScore[bit][currentNode]
                    currentNode = jumpTo[bit][currentNode]

            maxScore = max(maxScore, currentScore)

        return maxScore