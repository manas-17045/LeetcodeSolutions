# Leetcode 1665: Minimum Initial Energy to Finish Tasks
# https://leetcode.com/problems/minimum-initial-energy-to-finish-tasks/
# Solved on 7th of August, 2025
class Solution:
    def minimumEffort(self, tasks: list[list[int]]) -> int:
        """
        Calculates the minimum initial energy required to complete all tasks.

        Args:
            tasks: A list of tasks, where each task is a list of two integers:
                   [actual_cost, minimum_requirement].

        Returns:
            The minimum initial energy required to complete all tasks.
        """
        tasks.sort(key=lambda task: task[1] - task[0], reverse=True)

        requiredEnergy = 0
        for task in reversed(tasks):
            actualCost = task[0]
            minimumRequirement = task[1]
            requiredEnergy = max(minimumRequirement, (requiredEnergy + actualCost))

        return requiredEnergy