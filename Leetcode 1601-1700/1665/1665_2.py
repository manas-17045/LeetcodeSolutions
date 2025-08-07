# Leetcode 1665: Minimum Initial Energy to Finish Tasks
# https://leetcode.com/problems/minimum-initial-energy-to-finish-tasks/
# Solved on 7th of August, 2025
class Solution:
    def minimumEffort(self, tasks: list[list[int]]) -> int:
        """
        Calculates the minimum initial energy required to complete all tasks.

        Args:
            tasks: A list of tasks, where each task is a list of two integers:
                   [actual_energy_cost, minimum_energy_requirement].

        Returns:
            The minimum initial energy required to complete all tasks.
        """
        # Sort by (minimum - actual) descending, tiebreak on minimum descending
        tasks.sort(key=lambda t: (t[1] - t[0], t[1]), reverse=True)

        # Total extra energy we have pumped in so far
        initial = 0
        # Our current energy at each step
        current = 0

        for actual, minimum in tasks:
            if current < minimum:
                # We need to increase our starting pool by (minimum - current)
                diff = minimum - current
                initial += diff
                current += diff

            # Do the task
            current -= actual

        return initial