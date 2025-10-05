# Leetcode 3594: Minimum Time to Transport All Individuals
# https://leetcode.com/problems/minimum-time-to-transport-all-individuals/
# Solved on 5th of October, 2025
import heapq
import math
from itertools import combinations


class Solution:
    def minTime(self, n: int, k: int, m: int, time: list[int], mul: list[float]) -> float:
        """
        Calculates the minimum time to complete a series of tasks.
        :param n: The total number of tasks.
        :param k: The maximum number of tasks that can be picked up at once.
        :param m: The modulo for stage advancement.
        :param time: A list of integers representing the time required for each task.
        :param mul: A list of floats representing the multiplier for each stage.
        :return: The minimum time as a float, or -1 if it's not possible to complete all tasks.
        """

        ALL = (1 << n) - 1
        dist = [[[float('inf')] * 2 for _ in range(m)] for _ in range(1 << n)]
        dist[0][0][0] = 0
        pq = [(0, 0, 0, 0)]  # d, mask, stg, bt
        ans = float('inf')

        while pq:
            d, mask, stg, bt = heapq.heappop(pq)
            if d > dist[mask][stg][bt]:
                continue
            if mask == ALL and bt == 1:
                ans = min(ans, d)
                continue
            if bt == 0:
                at_start_mask = ALL ^ mask
                if at_start_mask == 0:
                    continue
                at_start = [i for i in range(n) if at_start_mask & (1 << i)]

                for r in range(1, min(k, len(at_start)) + 1):
                    for comb in combinations(at_start, r):
                        max_t = max(time[j] for j in comb)
                        trip = max_t * mul[stg]
                        new_d = d + trip
                        if new_d >= ans:
                            continue
                        adv = math.floor(trip) % m
                        new_stg = (stg + adv) % m
                        new_mask = mask
                        for j in comb:
                            new_mask |= (1 << j)
                        new_bt = 1
                        if new_d < dist[new_mask][new_stg][new_bt]:
                            dist[new_mask][new_stg][new_bt] = new_d
                            heapq.heappush(pq, (new_d, new_mask, new_stg, new_bt))

            else:
                if mask == ALL:
                    continue
                at_dest = [i for i in range(n) if mask & (1 << i)]
                for r in at_dest:
                    trip = time[r] * mul[stg]
                    new_d = d + trip
                    if new_d >= ans:
                        continue
                    adv = math.floor(trip) % m
                    new_stg = (stg + adv) % m
                    new_mask = mask ^ (1 << r)
                    new_bt = 0
                    if new_d < dist[new_mask][new_stg][new_bt]:
                        dist[new_mask][new_stg][new_bt] = new_d
                        heapq.heappush(pq, (new_d, new_mask, new_stg, new_bt))

        return ans if ans < float('inf') else -1