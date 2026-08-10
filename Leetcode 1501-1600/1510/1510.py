# Leetcode 1510: Stone Game IV
# https://leetcode.com/problems/stone-game-iv/
# Solved on 10th of August, 2026
class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        """
        Determines if Alice wins the stone game IV.
        
        @param n: The initial number of stones.
        @return: True if Alice wins, false otherwise.
        """
        dpTable = [False] * (n + 1)

        for stoneCount in range(1, n + 1):
            squareNum = 1
            while squareNum * squareNum <= stoneCount:
                if not dpTable[stoneCount - squareNum * squareNum]:
                    dpTable[stoneCount] = True
                    break
                
                squareNum += 1

            return dpTable[n]