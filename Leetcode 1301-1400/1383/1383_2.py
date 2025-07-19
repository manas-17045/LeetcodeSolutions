# Leetcode 1383: Maximum Performance of a Team
# https://leetcode.com/problems/maximum-performance-of-a-team/
# Solved on 19th of July, 2025
import heapq


class Solution:
    def maxPerformance(self, n: int, speed: list[int], efficiency: list[int], k: int) -> int:
        """
        Calculates the maximum performance of a team of engineers.

        Args:
            n (int): The total number of engineers.
            speed (list[int]): A list of speeds for each engineer.
            efficiency (list[int]): A list of efficiencies for each engineer.
            k (int): The maximum number of engineers allowed in the team.
        """
        MOD = 10**9 + 7
        engineers = sorted(zip(efficiency, speed), reverse=True)
        speed_heap = []
        speed_sum = 0
        result = 0
        for curr_effi, curr_speed in engineers:
            heapq.heappush(speed_heap, curr_speed)
            speed_sum += curr_speed
            if len(speed_heap) > k:
                speed_sum -= heapq.heappop(speed_heap)
            result = max(result, speed_sum * curr_effi)
        return result % MOD