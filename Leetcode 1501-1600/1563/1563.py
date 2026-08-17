# Leetcode 1563: Stone Game V
# https://leetcode.com/problems/stone-game-v/
# Solved on 17th of August, 2026
class Solution:
    def stoneGameV(self, stoneValue: list[int]) -> int:
        """
        Calculates the maximum score possible in the Stone Game V.
        
        Args:
            stoneValue: The values of the stones.
            
        Returns:
            The maximum score possible.
        """
        stoneCount = len(stoneValue)
        if stoneCount <= 1:
            return 0

        prefixSum = [0] * (stoneCount + 1)
        for index in range(stoneCount):
            prefixSum[index + 1] = prefixSum[index] + stoneValue[index]

        maxLeft = [[0] * stoneCount for _ in range(stoneCount)]
        maxRight = [[0] * stoneCount for _ in range(stoneCount)]
        dpTable = [[0] * stoneCount for _ in range(stoneCount)]

        for leftIndex in range(stoneCount - 1, -1, -1):
            maxLeft[leftIndex][leftIndex] = stoneValue[leftIndex]
            maxRight[leftIndex][leftIndex] = stoneValue[leftIndex]
            splitIndex = leftIndex - 1

            for rightIndex in range(leftIndex + 1, stoneCount):
                totalSum = prefixSum[rightIndex + 1] - prefixSum[leftIndex]

                while splitIndex + 1 < rightIndex and 2 * (prefixSum[splitIndex + 2] - prefixSum[leftIndex]) <= totalSum:
                    splitIndex += 1

                if splitIndex >= leftIndex and 2 * (prefixSum[splitIndex + 1] - prefixSum[leftIndex]) == totalSum:
                    leftOption = maxLeft[leftIndex][splitIndex]
                    rightOption = maxRight[splitIndex + 1][rightIndex]
                    dpTable[leftIndex][rightIndex] = max(leftOption, rightOption)
                else:
                    leftOption = maxLeft[leftIndex][splitIndex] if splitIndex >= leftIndex else 0
                    rightOption = maxRight[splitIndex + 2][rightIndex] if splitIndex + 2 <= rightIndex else 0
                    dpTable[leftIndex][rightIndex] = max(leftOption, rightOption)

                currentScore = totalSum + dpTable[leftIndex][rightIndex]
                maxLeft[leftIndex][rightIndex] = max(maxLeft[leftIndex][rightIndex - 1], currentScore)
                maxRight[leftIndex][rightIndex] = max(maxRight[leftIndex + 1][rightIndex], currentScore)

        return dpTable[0][stoneCount - 1]