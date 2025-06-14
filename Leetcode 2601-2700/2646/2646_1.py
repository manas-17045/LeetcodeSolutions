# Leetcode 2646: Minimize the Total Price of the Trips
# https://leetcode.com/problems/minimize-the-total-price-of-the-trips/
# Solved on 14th of June, 2025
import collections


class Solution:
    def minimumTotalPrice(self, n: int, edges: list[list[int]], price: list[int], trips: list[list[int]]) -> int:
        """
        Calculates the minimum total price of all trips by deciding whether to halve the price of each node.

        The problem can be broken down into two main parts:

        1. Calculate the number of times each node is visited across all trips.

        2. Use dynamic programming on the tree structure to determine the maximum savings achievable by halving node
        prices, with the constraint that adjacent nodes cannot both have their prices halved.

        Args:
            n: The number of nodes in the tree.
            edges: A list of edges representing the tree.
            price: A list of prices for each node.
            trips: A list of trips, where each trip is a pair of start and end nodes.

        Returns:
            The minimum total price of all trips.
        """
        adjacencyList = collections.defaultdict(list)
        for u, v in edges:
            adjacencyList[u].append(v)
            adjacencyList[v].append(u)

        nodeVisitCounts = [0] * n
        for startNode, endNode in trips:
            parentTracker = [-1] * n
            bfsQueue = collections.deque([startNode])
            visitedNodes = {startNode}

            while bfsQueue:
                u = bfsQueue.popleft()
                if u == endNode:
                    break
                for v in adjacencyList[u]:
                    if v not in visitedNodes:
                        visitedNodes.add(v)
                        parentTracker[v] = u
                        bfsQueue.append(v)

            currentNode = endNode
            while currentNode != -1:
                nodeVisitCounts[currentNode] += 1
                currentNode = parentTracker[currentNode]

        def findMaxSavings(node, parent):
            savingsIfHalved = (price[node] * nodeVisitCounts[node]) // 2
            savingsIfNotHalved = 0

            for neighbor in adjacencyList[node]:
                if neighbor == parent:
                    continue

                childHalved, childNotHalved = findMaxSavings(neighbor, node)

                savingsIfHalved += childHalved
                savingsIfNotHalved += max(childHalved, childNotHalved)


            return savingsIfHalved, savingsIfNotHalved

        initialTotalPrice = 0
        for i in range(n):
            initialTotalPrice += price[i] * nodeVisitCounts[i]

        halved, notHalved = findMaxSavings(0, -1)
        maxSavings = max(halved, notHalved)

        return initialTotalPrice - maxSavings