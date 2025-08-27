# Leetcode 2008: Maximum Earnings From Taxi
# https://leetcode.com/problems/maximum-earnings-from-taxi/
# Solved on 27th of August, 2025
import collections


class Solution:
    def maxTaxiEarnings(self, n: int, rides: list[list[int]]) -> int:
        """
        Calculates the maximum earnings a taxi driver can make given a set of rides.

        Args:
            n (int): The maximum point a taxi can reach.
            rides (list[list[int]]): A list of rides, where each ride is [start_point, end_point, tip].
        Returns:
            int: The maximum earnings achievable.
        """
        ridesByEndPoint = collections.defaultdict(list)
        for start, end, tip in rides:
            rideProfit = end - start + tip
            ridesByEndPoint[end].append((start, rideProfit))

        maxEarningsUpTo = [0] * (n + 1)

        for currentPoint in range(1, n + 1):
            maxEarningsUpTo[currentPoint] = maxEarningsUpTo[currentPoint - 1]

            if currentPoint in ridesByEndPoint:
                for startPoint, rideProfit in ridesByEndPoint[currentPoint]:
                    potentialEarning = maxEarningsUpTo[startPoint] + rideProfit
                    maxEarningsUpTo[currentPoint] = max(maxEarningsUpTo[currentPoint], potentialEarning)

        return maxEarningsUpTo[n]