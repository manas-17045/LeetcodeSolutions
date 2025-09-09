# Leetcode 1701: Average Waiting Time
# https://leetcode.com/problems/average-waiting-time/
# Solved on 9th of September, 2025
class Solution:
    def averageWaitingTime(self, customers: list[list[int]]) -> float:
        """
        Calculates the average waiting time for customers.
        :param customers: A list of lists, where each inner list contains [arrival_time, preparation_time].
        :return: The average waiting time as a float.
        """
        current_time = 0
        total_wait = 0

        for arrival, prep in customers:
            # Chef starts when free or when customer arrives
            start = max(current_time, arrival)
            finish = start + prep
            total_wait += (finish - arrival)
            current_time = finish

        return total_wait / len(customers)