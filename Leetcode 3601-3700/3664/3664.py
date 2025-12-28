# Leetcode 3664: Two-Letter Card Game
# https://leetcode.com/problems/two-letter-card-game/
# Solved on 28th of December, 2025
class Solution:
    def score(self, cards: list[str], x: str) -> int:
        """
        Calculates the maximum possible score in a two-letter card game.

        Args:
            cards: A list of strings, where each string represents a two-letter card.
            x: A single character representing the special letter.
        Returns:
            The maximum possible score.
        """
        xxCount = 0
        startSum = 0
        startMax = 0
        endSum = 0
        endMax = 0

        startFreq = {}
        endFreq = {}

        for card in cards:
            c0 = card[0]
            c1 = card[1]

            if c0 == x and c1 == x:
                xxCount += 1
            elif c0 == x:
                startFreq[c1] = startFreq.get(c1, 0) + 1
                startSum += 1
                if startFreq[c1] > startMax:
                    startMax = startFreq[c1]
            elif c1 == x:
                endFreq[c0] = endFreq.get(c0, 0) + 1
                endSum += 1
                if endFreq[c0] > endMax:
                    endMax = endFreq[c0]

        maxPoints = 0

        for i in range(xxCount + 1):
            currentStartSum = startSum + i
            currentStartMax = max(startMax, i)
            startPoints = min(currentStartSum // 2, currentStartSum - currentStartMax)

            xxInEnd = xxCount - i
            currentEndSum = endSum + xxInEnd
            currentEndMax = max(endMax, xxInEnd)
            endPoints = min(currentEndSum // 2, currentEndSum - currentEndMax)

            if startPoints + endPoints > maxPoints:
                maxPoints = startPoints + endPoints

        return maxPoints