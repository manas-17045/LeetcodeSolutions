# Leetcode 1701: Average Waiting Time
# https://leetcode.com/problems/average-waiting-time/
# Solved on 9th of September, 2025
class Solution:
    def averageWaitingTime(self, customers: list[list[int]]) -> float:
        """
        Calculates the average waiting time for all customers.

        Args:
            customers: A list of lists, where each inner list `[arrivalTime, cookTime]`
                       represents a customer's arrival time and the time it takes to cook their order.
        Returns:
            The average waiting time across all customers.
        """
        totalWaitTime = 0.0
        chefAvailableTime = 0

        for arrivalTime, cookTime in customers:
            startTime = max(arrivalTime, chefAvailableTime)

            finishTime = startTime + cookTime

            waitTime = finishTime - arrivalTime
            totalWaitTime += waitTime

            chefAvailableTime = finishTime

        return totalWaitTime / len(customers)