# Leetcode 1200: Minimum Absolute Difference
# https://leetcode.com/problems/minimum-absolute-difference/
# Solved on 26th of January, 2026
class Solution:
    def minimumAbsDifference(self, arr: list[int]) -> list[list[int]]:
        """
        Finds all pairs of elements with the minimum absolute difference.

        Args:
            arr (list[int]): A list of distinct integers.

        Returns:
            list[list[int]]: A list of pairs [a, b] such that a < b and b - a is the minimum absolute difference.
        """
        arr.sort()

        minDiff = float('inf')
        resultList = []
        for i in range(len(arr) - 1):
            currentDiff = arr[i + 1] - arr[i]

            if currentDiff < minDiff:
                minDiff = currentDiff
                resultList = [[arr[i], arr[i + 1]]]
            elif currentDiff == minDiff:
                resultList.append([arr[i], arr[i + 1]])

        return resultList