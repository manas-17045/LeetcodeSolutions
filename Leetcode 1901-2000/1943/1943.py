# Leetcode 1943: Describe the Painting
# https://leetcode.com/problems/describe-the-painting/
# Solved on 5th of November, 2025
import collections


class Solution:
    def splitPainting(self, segments: list[list[int]]) -> list[list[int]]:
        """
        Given a list of segments, where each segment is represented as [start, end, color],
        describes the painting by returning a list of segments that represent the final
        painting after all segments are applied.

        Args:
            segments: A list of segments, where each segment is [start, end, color].
        Returns:
            A list of segments representing the final painting, where each segment is [start, end, color].
        """
        colorChanges = collections.defaultdict(int)

        for start, end, color in segments:
            colorChanges[start] += color
            colorChanges[end] -= color

        sortedPoints = sorted(colorChanges.keys())

        result = []
        currentColor = 0
        previousPoint = None

        for currentPoint in sortedPoints:
            if previousPoint is not None and currentColor > 0:
                result.append([previousPoint, currentPoint, currentColor])

            currentColor += colorChanges[currentPoint]
            previousPoint = currentPoint

        return result