# Leetcode 1140: Stone Game II
# https://leetcode.com/problems/stone-game-ii/
# Solved on 9th of August, 2026
class Solution:
    def stoneGameII(self, piles: list[int]) -> int:
        """
        Determines the maximum number of stones the first player can get in the Stone Game II.
        
        Args:
            piles: Array of piles of stones.
        
        Returns:
            Maximum stones the first player can get.
        """
        pilesCount = len(piles)
        suffixSum = [0] * (pilesCount + 1)

        for pileIndex in range(pilesCount - 1, -1, -1):
            suffixSum[pileIndex] = suffixSum[pileIndex + 1] + piles[pileIndex]
        
        dpTable = [[0] * (pilesCount + 1) for _ in range(pilesCount + 1)]

        for pileIndex in range(pilesCount - 1, -1, -1):
            for currentM in range(pilesCount, 0, -1):
                if pileIndex + 2 * currentM >= pilesCount:
                    dpTable[pileIndex][currentM] = suffixSum[pileIndex]
                else:
                    for moveSize in range(1, 2 * currentM + 1):
                        nextM = max(currentM, moveSize)
                        dpTable[pileIndex][currentM] = max(
                            dpTable[pileIndex][currentM],
                            suffixSum[pileIndex] - dpTable[pileIndex + moveSize][nextM]
                        )

        return dpTable[0][1]