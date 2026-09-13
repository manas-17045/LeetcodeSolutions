# Leetcode 835: Image Overlap
# https://leetcode.com/problems/image-overlap/
# Solved on 13th of September, 2026
from collections import defaultdict


class Solution:
    def largestOverlap(self, img1: list[list[int]], img2: list[list[int]]) -> int:
        """
        Calculates the maximum possible overlap of 1s between two binary images
        after translation.

        Parameters:
            img1 (list[list[int]]): First binary square matrix.
            img2 (list[list[int]]): Second binary square matrix.

        Returns:
            int: Maximum number of overlapping 1s between the two images.
        """
        gridSize = len(img1)
        firstImageOnes = []
        secondImageOnes = []

        for rowIdx in range(gridSize):
            for colIdx in range(gridSize):
                if img1[rowIdx][colIdx] == 1:
                    firstImageOnes.append((rowIdx, colIdx))
                if img2[rowIdx][colIdx] == 1:
                    secondImageOnes.append((rowIdx, colIdx))

        if not firstImageOnes or not secondImageOnes:
            return 0

        vectorCounts = defaultdict(int)
        maxOverlap = 0

        for rowOne, colOne in firstImageOnes:
            for rowTwo, colTwo in secondImageOnes:
                vectorKey = (rowOne - rowTwo, colOne - colTwo)
                vectorCounts[vectorKey] += 1
                if vectorCounts[vectorKey] > maxOverlap:
                    maxOverlap = vectorCounts[vectorKey]

        return maxOverlap