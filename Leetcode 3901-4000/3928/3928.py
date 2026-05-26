# Leetcode 3928: Minimum Cost to Buy Apples II
# https://leetcode.com/problems/minimum-cost-to-buy-apples-ii/
# Solved on 26th of May, 2026
import heapq


class Solution:
    def minCost(self, n: int, prices: list[int], roads: list[list[int]]) -> list[int]:
        """
        Calculates the minimum cost to buy apples for each city.

        :param n: The number of cities.
        :param prices: A list of apple prices in each city.
        :param roads: A list of roads where each road is [u, v, cost, multiplier].
        :return: A list of minimum costs for each starting city.
        """
        adjOne = [[] for _ in range(n)]
        adjTwo = [[] for _ in range(n)]

        for startNode, endNode, travelCost, taxMultiplier in roads:
            adjOne[startNode].append((endNode, travelCost))
            adjOne[endNode].append((startNode, travelCost))
            adjTwo[startNode].append((endNode, travelCost * taxMultiplier))
            adjTwo[endNode].append((startNode, travelCost * taxMultiplier))

        ansArray = []
        infinityVal = float('inf')

        for startShop in range(n):
            distOne = [infinityVal] * n
            distOne[startShop] = 0
            pqOne = [(0, startShop)]

            while pqOne:
                currentDist, currentNode = heapq.heappop(pqOne)

                if currentDist > distOne[currentNode]:
                    continue

                for nextNode, edgeWeight in adjOne[currentNode]:
                    if distOne[nextNode] > currentDist + edgeWeight:
                        distOne[nextNode] = currentDist + edgeWeight
                        heapq.heappush(pqOne, (distOne[nextNode], nextNode))

            distTwo = [infinityVal] * n
            distTwo[startShop] = 0
            pqTwo = [(0, startShop)]

            while pqTwo:
                currentDist, currentNode = heapq.heappop(pqTwo)

                if currentDist > distTwo[currentNode]:
                    continue

                for nextNode, edgeWeight in adjTwo[currentNode]:
                    if distTwo[nextNode] > currentDist + edgeWeight:
                        distTwo[nextNode] = currentDist + edgeWeight
                        heapq.heappush(pqTwo, (distTwo[nextNode], nextNode))

            minTotalCost = infinityVal

            for targetShop in range(n):
                currentTotal = distOne[targetShop] + distTwo[targetShop] + prices[targetShop]
                if currentTotal < minTotalCost:
                    minTotalCost = currentTotal

            ansArray.append(minTotalCost)

        return ansArray