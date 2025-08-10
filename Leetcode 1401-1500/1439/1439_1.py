# Leetcode 1439: Find the Kth Smallest Sum of a Matrix With Sorted Rows
# https://leetcode.com/problems/find-the-kth-smallest-sum-of-a-matrix-with-sorted-rows/
# Solved on 10th of August, 2025
import heapq


class Solution:
    def kthSmallest(self, mat: list[list[int]], k: int) -> int:
        """
        Finds the Kth smallest sum of a matrix with sorted rows.

        Args:
            mat (list[list[int]]): A matrix where each row is sorted in non-decreasing order.
            k (int): The desired Kth smallest sum.
        Returns:
            int: The Kth smallest sum.
        """

        sums = mat[0]
        numRows = len(mat)

        for i in range(1, numRows):
            currentRow = mat[i]
            numCols = len(currentRow)
            minHeap = []

            for j in range(len(sums)):
                heapq.heappush(minHeap, (sums[j] + currentRow[0], j, 0))

            newSums = []
            while minHeap and len(newSums) < k:
                sumVal, prevSumIndex, currentRowIndex = heapq.heappop(minHeap)
                newSums.append(sumVal)

                if currentRowIndex + 1 < numCols:
                    nextSum = sums[prevSumIndex] + currentRow[currentRowIndex + 1]
                    heapq.heappush(minHeap, (nextSum, prevSumIndex, currentRowIndex + 1))

            sums = newSums

        return sums[k - 1]