# Leetcode 1488: Avoid Flood in The City
# https://leetcode.com/problems/avoid-flood-in-the-city/
# Resolved on 7th of october, 2025
import heapq


class Solution:
    def avoidFlood(self, rains: list[int]) -> list[int]:
        """
        Given an array `rains` representing the daily rainfall, where `rains[i]` is the lake that
        rains on day `i` (if `rains[i] > 0`) or a dry day (if `rains[i] == 0`).
        Return an array `ans` where `ans[i]` is the lake to dry on day `i` if it's a dry day,
        or -1 if it's a rainy day. If it's impossible to avoid a flood, return an empty array.

        :param rains: A list of integers representing the rainfall on each day.
        :return: A list of integers representing the drying schedule, or an empty list if impossible.
        """
        n = len(rains)
        ans = [1] * n

        nextRain = {}
        lastSeen = {}
        for i in range(n - 1, -1, -1):
            lake = rains[i]
            if lake > 0:
                if lake in lastSeen:
                    nextRain[i] = lastSeen[lake]
                lastSeen[lake] = i

        fullLakes = set()
        dryingTasks = []

        for i in range(n):
            lake = rains[i]

            if lake == 0:
                if dryingTasks:
                    _, lakeToDry = heapq.heappop(dryingTasks)
                    ans[i] = lakeToDry
                    fullLakes.remove(lakeToDry)
            else:
                ans[i] = -1
                if lake in fullLakes:
                    return []

                fullLakes.add(lake)
                if lake in nextRain:
                    heapq.heappush(dryingTasks, (nextRain[lake], lake))

        return ans