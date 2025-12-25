# Leetcode 3776: Minimum Moves to Balance Circular Array
# https://leetcode.com/problems/minimum-moves-to-balance-circular-array/
# Solved on 25th of December, 2025
class Solution:
    def minMoves(self, balance: list[int]) -> int:
        """
        Calculates the minimum moves to balance a circular array.

        Args:
            balance: A list of integers representing the balance at each position in the circular array.
        Returns:
            The minimum number of moves required to balance the array, or -1 if it's impossible.
        """
        currentSum = sum(balance)
        if currentSum < 0:
            return -1

        n = len(balance)
        negativeIndex = -1

        for i in range(n):
            if balance[i] < 0:
                negativeIndex = i
                break

        if negativeIndex == -1:
            return 0

        neededAmount = -balance[negativeIndex]
        totalMoves = 0

        for distance in range(1, n // 2 + 1):
            if neededAmount == 0:
                break

            leftIndex = (negativeIndex - distance) % n
            if balance[leftIndex] > 0:
                amountToTake = min(neededAmount, balance[leftIndex])
                totalMoves += amountToTake * distance
                neededAmount -= amountToTake

            if neededAmount == 0:
                break

            rightIndex = (negativeIndex + distance) % n
            if leftIndex != rightIndex and balance[rightIndex] > 0:
                amountToTake = min(neededAmount, balance[rightIndex])
                totalMoves += amountToTake * distance
                neededAmount -= amountToTake

        return totalMoves