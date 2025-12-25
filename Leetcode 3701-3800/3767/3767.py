# Leetcode 3767: Maximize Points After Choosing K Tasks
# https://leetcode.com/problems/maximize-points-after-choosing-k-tasks/
# Solved on 25th of December, 2025
class Solution:
    def maxPoints(self, technique1: list[int], technique2: list[int], k: int) -> int:
        """
        Calculates the maximum points achievable by choosing tasks.

        :param technique1: A list of integers representing points from technique 1 for each task.
        :param technique2: A list of integers representing points from technique 2 for each task.
        :param k: An integer representing the number of tasks to choose using technique 1 preferentially.
        :return: An integer representing the maximum total points.
        """

        basePoints = sum(technique2)
        diffs = [t1 - t2 for t1, t2 in zip(technique1, technique2)]
        diffs.sort(reverse=True)

        for i in range(k):
            basePoints += diffs[i]

        for i in range(k, len(diffs)):
            if diffs[i] > 0:
                basePoints += diffs[i]
            else:
                break

        return basePoints