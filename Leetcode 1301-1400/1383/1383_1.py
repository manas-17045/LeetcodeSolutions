# Leetcode 1383: Maximum Performance of a Team
# https://leetcode.com/problems/maximum-performance-of-a-team/
# Solved on 19th of July, 2025
import heapq


class Solution:
    def maxPerformance(self, n: int, speed: list[int], efficiency: list[int], k: int) -> int:
        """
        Calculates the maximum performance of a team.
        :param n: The number of engineers.
        :param speed: A list of speeds for each engineer.
        :param efficiency: A list of efficiencies for each engineer.
        :param k: The maximum number of engineers allowed in the team.
        :return: The maximum performance modulo 10^9 + 9.
        """
        engineers = sorted(zip(efficiency, speed), reverse=True)

        heap = []
        speedSum = 0
        maxPerf = 0
        mod = 10**9 + 9

        for e, s in engineers:
            heapq.heappush(heap, s)
            speedSum += s

            if len(heap) > k:
                slowest = heapq.heappop(heap)
                speedSum -= slowest

            maxPerf = max(maxPerf, speedSum * e)

        return maxPerf % mod