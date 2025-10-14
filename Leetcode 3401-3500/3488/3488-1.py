# Leetcode 3488: Closest Equal Element Queries
# https://leetcode.com/problems/closest-equal-element-queries/
# Solved on 14th of October, 2025
class Solution:
    def solveQueries(self, nums: list[int], queries: list[int]) -> list[int]:
        """
        Finds the distance to the closest equal element for each query index in a circular array.

        Args:
            nums: A list of integers representing the circular array.
            queries: A list of integers, where each integer is an index to query.
        Returns:
            A list of integers, where each element is the minimum distance to an equal element for the corresponding query.
            If no equal element exists, -1 is returned.
        """
        listSize = len(nums)

        precomputeDistances = [float('inf')] * listSize
        lastSeenIndex = {}

        for i in range(listSize * 2):
            currentValue = nums[i % listSize]
            currentIndex = i % listSize
            if currentValue in lastSeenIndex:
                distance = i - lastSeenIndex[currentValue]
                precomputeDistances[currentIndex] = min(precomputeDistances[currentIndex], distance)
            lastSeenIndex[currentValue] = i

        lastSeenIndex.clear()

        for i in range(listSize * 2 - 1, -1, -1):
            currentValue = nums[i % listSize]
            currentIndex = i % listSize
            if currentValue in lastSeenIndex:
                distance = lastSeenIndex[currentValue] - i
                precomputeDistances[currentIndex] = min(precomputeDistances[currentIndex], distance)
            lastSeenIndex[currentValue] = i

        queryResults = []
        for query in queries:
            distance = precomputeDistances[query]
            queryResults.append(-1 if distance >= listSize else int(distance))

        return queryResults