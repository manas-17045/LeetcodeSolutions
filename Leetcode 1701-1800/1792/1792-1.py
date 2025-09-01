# Leetcode 1792: Maximum Average Pass Ratio
# https://leetcode.com/problems/maximum-average-pass-ratio/
# Resolved on 1st of September, 2025
import heapq


class Solution:
    def maxAverageRatio(self, classes: list[list[int]], extraStudents: int) -> float:
        """
        Calculates the maximum average pass ratio after adding `extraStudents` to the classes.

        Args:
            classes (list[list[int]]): A list where each inner list `[passCount, totalCount]`
                                       represents the number of passing students and total students in a class.
            extraStudents (int): The number of additional students that can be assigned to classes.

        Returns:
            float: The maximum possible average pass ratio.
        """
        maxHeap = []

        for passCount, totalCount in classes:
            gain = (totalCount - passCount) / (totalCount * (totalCount + 1))
            heapq.heappush(maxHeap, (-gain, passCount, totalCount))

        for _ in range(extraStudents):
            negGain, passCount, totalCount = heapq.heappop(maxHeap)

            passCount += 1
            totalCount += 1

            newGain = (totalCount - passCount) / (totalCount * (totalCount + 1))
            heapq.heappush(maxHeap, (-newGain, passCount, totalCount))

        totalRatio = 0
        for _, passCount, totalCount in maxHeap:
            totalRatio += passCount / totalCount

        return totalRatio / len(classes)