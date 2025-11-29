# Leetcode 2121: Intervals Between Identical Elements
# https://leetcode.com/problems/intervals-between-identical-elements/
# Solved on 29th of November, 2025
class Solution:
    def getDistances(self, arr: list[int]) -> list[int]:
        """
        Calculates the sum of absolute differences between the index of each element
        and the indices of all other identical elements in the array.

        Args:
            arr (list[int]): The input array of integers.
        Returns:
            list[int]: An array where each element intervals[i] is the sum of |i - j|
                       for all j such that arr[j] == arr[i] and j != i.
        """
        n = len(arr)
        intervals = [0] * n

        sumMap = {}
        countMap = {}

        for i in range(n):
            val = arr[i]
            if val not in sumMap:
                sumMap[val] = 0
                countMap[val] = 0

            intervals[i] += (countMap[val] * i) - sumMap[val]
            sumMap[val] += i
            countMap[val] += 1

        sumMap = {}
        countMap = {}

        for i in range(n - 1, -1, -1):
            val = arr[i]
            if val not in sumMap:
                sumMap[val] = 0
                countMap[val] = 0

            intervals[i] += sumMap[val] - (countMap[val] * i)
            sumMap[val] += i
            countMap[val] += 1

        return intervals