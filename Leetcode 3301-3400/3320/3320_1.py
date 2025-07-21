# Leetcode 3320: Count The Number of Winning Sequences
# https://leetcode.com/problems/count-the-number-of-winning-sequences/
# Solved on 21st of July, 2025
class Solution:
    def countWinningSequences(self, s: str) -> int:
        """
        Counts the number of winning sequences for Bob.

        Args:
            s (str): A string representing Alice's sequence of moves ('F', 'W', 'E').
        Returns:
            int: The number of winning sequences for Bob, modulo 1,000,000,007.
        """
        n = len(s)
        mod = 1_000_000_007

        charToIndex = {'F': 0, 'W': 1, 'E': 2}
        sAsIndices = [charToIndex[c] for c in s]

        def getScoreChange(bobMove, aliceMove):
            if (bobMove == 0 and aliceMove == 2) or (bobMove == 1 and aliceMove == 0) or (bobMove == 2 and aliceMove == 1):
                return 1
            elif (aliceMove == 0 and bobMove == 2) or (aliceMove == 1 and bobMove == 0) or (aliceMove == 2 and bobMove == 1):
                return -1
            else:
                return 0

        dp = [[0] * 3 for _ in range(2 * n + 1)]

        if n == 0:
            return 0

        aliceMove = sAsIndices[0]
        for bobMove in range(3):
            change = getScoreChange(bobMove, aliceMove)
            dp[change + n][bobMove] = 1

        for i in range(1, n):
            nextDp = [[0] * 3 for _ in range(2 * n + 1)]
            aliceMove = sAsIndices[i]

            maxDiff = i
            for diff in range(-maxDiff, maxDiff + 1):
                diffOffset = diff + n
                for lastBobMove in range(3):
                    count = dp[diffOffset][lastBobMove]
                    if count == 0:
                        continue

                    for currentBobMove in range(3):
                        if currentBobMove == lastBobMove:
                            continue

                        change = getScoreChange(currentBobMove, aliceMove)
                        newDiff = diff + change
                        newDiffOffset = newDiff + n

                        nextDp[newDiffOffset][currentBobMove] = (nextDp[newDiffOffset][currentBobMove] + count) % mod
            dp = nextDp

        totalWins = 0
        for diff in range(1, n + 1):
            diffOffset = diff + n
            for lastBobMove in range(3):
                totalWins = (totalWins + dp[diffOffset][lastBobMove]) % mod

        return totalWins