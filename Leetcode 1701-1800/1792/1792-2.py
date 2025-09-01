# Leetcode 1792: Maximum Average Pass Ratio
# https://leetcode.com/problems/maximum-average-pass-ratio/
# Solved on 1st of September, 2025
import heapq


class Solution:
    def maxAverageRatio(self, classes: list[list[int]], extraStudents: int) -> float:
        """
        Calculates the maximum average pass ratio after adding extra students.
        :param classes: A list of lists, where each inner list [p, t] represents a class with p passing students out of t total students.
        :param extraStudents: The number of extra students that can be assigned to classes.
        :return: The maximum possible average pass ratio.
        """
        def gain(p: int, t: int) -> float:
            # Marginal gain of adding one guaranteed-pass student to (p, t)
            return (p + 1) / (t + 1) - p / t

        # Build max-heap using negative values because heapq is a min-heap.
        heap = []
        total = 0.0
        for p, t in classes:
            total += p / t
            # Store (-gain, p, t), so we can pop the largest gain.
            heapq.heappush(heap, (-gain(p, t), p, t))

        for _ in range(extraStudents):
            neg_gain, p, t = heapq.heappop(heap)
            # Apply the best gain to the total average
            best_gain = -neg_gain
            total += best_gain
            # Update class (one more passing student and one more total)
            p += 1
            t += 1
            # Push updated class back with its new marginal gain
            heapq.heappush(heap, (-gain(p, t), p, t))

        # Average pass ratio is sum of class ratios divided by number of classes
        return total / len(classes)