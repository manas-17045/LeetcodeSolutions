# Leetcode 3347: Maximum Frequency of an Element After Performing Operations II
# https://leetcode.com/problems/maximum-frequency-of-an-element-after-performing-operations-ii/
# Solved on 22nd of October, 2025
import collections


class Solution:
    def maxFrequency(self, nums: list[int], k: int, numOperations: int) -> int:
        """
        Calculates the maximum frequency of an element in `nums` after performing at most `numOperations` operations.
        An operation consists of increasing an element by at most `k`.
        :param nums: A list of integers.
        :param k: The maximum value an element can be increased by in a single operation.
        :param numOperations: The maximum number of operations allowed.
        :return: The maximum possible frequency of an element.
        """
        initialCounts = collections.Counter(nums)
        differenceArray = collections.defaultdict(int)

        pointsOfInterest = set()

        for num in nums:
            pointsOfInterest.add(num)
            startPoint = num - k
            endPoint = num + k + 1

            differenceArray[startPoint] += 1
            differenceArray[endPoint] -= 1

            pointsOfInterest.add(startPoint)
            pointsOfInterest.add(endPoint)

        sortedPoints = sorted(list(pointsOfInterest.union(initialCounts.keys())))

        maxFreq = 0
        currentPotential = 0

        for point in sortedPoints:
            currentPotential += differenceArray[point]

            initialHere = initialCounts.get(point, 0)
            costHere = currentPotential - initialHere

            freqHere = initialHere + min(costHere, numOperations)
            maxFreq = max(maxFreq, freqHere)

        return maxFreq