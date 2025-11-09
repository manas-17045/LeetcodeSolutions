# Leetcode 2766: Relocate Marbles
# https://leetcode.com/problems/relocate-marbles/
# Solved on 9th of November, 2025
class Solution:
    def relocateMarbles(self, nums: list[int], moveFrom: list[int], moveTo: list[int]) -> list[int]:
        """
        Simulates the relocation of marbles and returns their final sorted positions.

        Args:
            nums: A list of integers representing the initial positions of the marbles.
            moveFrom: A list of integers where moveFrom[i] is the position a marble is moved from.
            moveTo: A list of integers where moveTo[i] is the position a marble is moved to.

        Returns:
            A sorted list of integers representing the final occupied positions of the marbles.
        """
        occupiedPositions = set(nums)

        numMoves = len(moveFrom)

        for i in range(numMoves):
            fromPos = moveFrom[i]
            toPos = moveTo[i]

            if fromPos in occupiedPositions:
                occupiedPositions.remove(fromPos)
                occupiedPositions.add(toPos)

        finalPositions = sorted(occupiedPositions)
        return finalPositions