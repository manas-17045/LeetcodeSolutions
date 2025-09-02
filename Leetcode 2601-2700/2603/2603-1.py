# Leetcode 2603: Collect Coins in a Tree
# https://leetcode.com/problems/collect-coins-in-a-tree/
# Solved on 2nd of September, 2025
import collections


class Solution:
    def collectTheCoins(self, coins: list[int], edges: list[list[int]]) -> int:
        """
        Collects coins in a tree by removing unnecessary nodes.

        Args:
            coins (list[int]): A list where coins[i] is 1 if the i-th node has a coin, and 0 otherwise.
            edges (list[list[int]]): A list of edges representing the tree structure.
        Returns:
            int: The minimum number of edges to traverse to collect all coins.
        """
        numberOfNodes = len(coins)
        if numberOfNodes <= 2:
            return 0

        adjacencyList = collections.defaultdict(list)
        nodeDegree = [0] * numberOfNodes
        for u, v in edges:
            adjacencyList[u].append(v)
            adjacencyList[v].append(u)
            nodeDegree[u] += 1
            nodeDegree[v] += 1

        removalQueue = collections.deque()
        for i in range(numberOfNodes):
            if nodeDegree[i] == 1 and coins[i] == 0:
                removalQueue.append(i)

        remainingNodes = numberOfNodes
        while removalQueue:
            currentNode = removalQueue.popleft()
            remainingNodes -= 1
            nodeDegree[currentNode] -= 1
            for neighborNode in adjacencyList[currentNode]:
                nodeDegree[neighborNode] -= 1
                if nodeDegree[neighborNode] == 1 and coins[neighborNode] == 0:
                    removalQueue.append(neighborNode)

        if remainingNodes <= 3:
            return 0

        leavesQueue = collections.deque()
        for i in range(numberOfNodes):
            if nodeDegree[i] == 1:
                leavesQueue.append(i)

        for _ in range(2):
            nodesInLevel = len(leavesQueue)
            if nodesInLevel == 0:
                break

            for _ in range(nodesInLevel):
                currentNode = leavesQueue.popleft()
                remainingNodes -= 1
                nodeDegree[currentNode] -= 1
                for neighborNode in adjacencyList[currentNode]:
                    nodeDegree[neighborNode] -= 1
                    if nodeDegree[neighborNode] == 1:
                        leavesQueue.append(neighborNode)

        return 0 if remainingNodes <= 1 else (remainingNodes - 1) * 2