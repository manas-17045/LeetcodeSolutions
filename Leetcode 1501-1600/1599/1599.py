# Leetcode 1599: Maximum Profit of Operating a Centennial Wheel
# https://leetcode.com/problems/maximum-profit-of-operating-a-centennial-wheel/
# Solved on 8th of December, 2025
class Solution:
    def minOperationsMaxProfit(self, customers: list[int], boardingCost: int, runningCost: int) -> int:
        """
        Calculates the maximum profit achievable from operating a Centennial Wheel and the minimum
        number of rotations to achieve that profit.

        Args:
            customers: A list of integers where customers[i] is the number of new customers arriving at rotation i.
            boardingCost: The cost to board one customer.
            runningCost: The cost to run the wheel for one rotation.

        Returns:
            The minimum number of rotations to achieve the maximum profit. If no profit can be made, return -1.
        """
        currentProfit = 0
        maxProfit = -1
        bestRotation = -1
        waitingCustomers = 0
        currentRotation = 0
        totalBoarded = 0

        for newCustomers in customers:
            waitingCustomers += newCustomers
            currentRotation += 1

            board = min(4, waitingCustomers)
            waitingCustomers -= board
            totalBoarded += board

            currentProfit = totalBoarded * boardingCost - currentRotation * runningCost

            if currentProfit > maxProfit:
                maxProfit = currentProfit
                bestRotation = currentRotation

        profitPerRotation = 4 * boardingCost - runningCost

        if waitingCustomers > 0 and profitPerRotation > 0:
            fullRotations = waitingCustomers // 4

            if fullRotations > 0:
                currentRotation += fullRotations
                totalBoarded += fullRotations * 4
                currentProfit += fullRotations * profitPerRotation

                if currentProfit > maxProfit:
                    maxProfit = currentProfit
                    bestRotation = currentRotation

            waitingCustomers %= 4

            if waitingCustomers > 0:
                currentRotation += 1
                totalBoarded += waitingCustomers
                currentProfit += waitingCustomers * boardingCost - runningCost

                if currentProfit > maxProfit:
                    maxProfit = currentProfit
                    bestRotation = currentRotation

        return bestRotation if maxProfit > 0 else -1