# Leetcode 1467: Probability of a Two Boxes Having The Same Number of Distinct Balls
# https://leetcode.com/problems/probability-of-a-two-boxes-having-the-same-number-of-distinct-balls/
# Solved on 8th of August, 2025
import collections


class Solution:
    def getProbability(self, balls: list[int]) -> float:
        """
        Calculates the probability that two boxes, each containing half of the total balls,
        have the same number of distinct ball colors.

        Args:
            balls (list[int]): A list where balls[i] is the number of balls of color i.
        Returns:
            float: The probability of having the same number of distinct ball colors in both boxes.
        """
        totalBallCount = sum(balls)
        halfBallCount = totalBallCount // 2

        memoCombinations = {}

        def getCombinations(n, k):
            if k < 0 or k > n:
                return 0
            if (n, k) in memoCombinations:
                return memoCombinations[(n, k)]
            if k == 0 or k == n:
                return 1
            if k > n // 2:
                k = n - k

            result = 1
            for i in range(k):
                result = result * (n - i) // (i + 1)
            memoCombinations[(n, k)] = result
            return result

        dpTable = collections.defaultdict(float)
        dpTable[(0, 0, 0)] = 1.0

        for colorCount in balls:
            newDpTable = collections.defaultdict(float)
            for state, numWays in dpTable.items():
                box1BallCount, box1DistinctCount, box2DistinctCount = state

                for ballsForBox1 in range(colorCount + 1):
                    if box1BallCount + ballsForBox1 > halfBallCount:
                        continue

                    ballsForBox2 = colorCount - ballsForBox1

                    nextBox1BallCount = box1BallCount + ballsForBox1
                    nextBox1DistinctCount = box1DistinctCount + (1 if ballsForBox1 > 0 else 0)
                    nextBox2DistinctCount = box2DistinctCount + (1 if ballsForBox2 > 0 else 0)

                    nextState = (nextBox1BallCount, nextBox1DistinctCount, nextBox2DistinctCount)

                    combCount = getCombinations(colorCount, ballsForBox1)
                    newDpTable[nextState] += numWays * combCount

            dpTable = newDpTable

        favorableOutcomes = 0.0
        for state, numWays in dpTable.items():
            box1BallCount, box1DistinctCount, box2DistinctCount = state
            if box1BallCount == halfBallCount and box1DistinctCount == box2DistinctCount:
                favorableOutcomes += numWays

        totalOutcomes = getCombinations(totalBallCount, halfBallCount)

        if totalOutcomes == 0:
            return 0.0

        return favorableOutcomes / totalOutcomes