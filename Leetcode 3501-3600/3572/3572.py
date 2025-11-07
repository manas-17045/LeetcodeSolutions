# Leetcode 3572: Maximize Y-Sum by Picking a Triplet of Distinct X-Values
# https://leetcode.com/problems/maximize-ysum-by-picking-a-triplet-of-distinct-xvalues/
# Solved on 7th of November, 2025
import collections


class Solution:
    def maxSumDistinctTriplet(self, x: list[int], y: list[int]) -> int:
        """
        Maximizes the sum of Y-values by picking a triplet of distinct X-values.

        Args:
            x (list[int]): A list of X-coordinates.
            y (list[int]): A list of Y-coordinates, where y[i] corresponds to x[i].

        Returns:
            int: The maximum possible sum of three Y-values corresponding to three distinct X-values.
                 Returns -1 if fewer than three distinct X-values are available.
        """
        groups = collections.defaultdict(list)
        n = len(x)

        for i in range(n):
            groups[x[i]].append(y[i])

        if len(groups) < 3:
            return -1

        topValues = []
        for xValue in groups:
            currentYValues = groups[xValue]
            currentYValues.sort(reverse=True)
            topForThisX = currentYValues[:3]
            for yValue in topForThisX:
                topValues.append((yValue, xValue))

        topValues.sort(reverse=True)

        chosenX = set()
        totalSum = 0
        count = 0

        for yValue, xValue in topValues:
            if xValue not in chosenX:
                totalSum += yValue
                chosenX.add(xValue)
                count += 1
                if count == 3:
                    break

        return totalSum