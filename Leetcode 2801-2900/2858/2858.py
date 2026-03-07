# Leetcode 2858: Minimum Edge Reversals So Every Node Is Reachable
# https://leetcode.com/problems/minimum-edge-reversals-so-every-node-is-reachable/
# Solved on 7th of March, 2026
class Solution:
    def minEdgeReversals(self, n: int, edges: list[list[int]]) -> list[int]:
        """
        Calculates the minimum number of edge reversals required for each node to be able to reach all other nodes.

        :param n: The number of nodes in the graph.
        :param edges: A list of directed edges represented as [u, v].
        :return: A list of integers where the i-th element is the minimum reversals needed for node i.
        """
        adjList = [[] for _ in range(n)]
        for u, v in edges:
            adjList[u].append((v, 0))
            adjList[v].append((u, 1))

        totalReversals = 0
        visitedNodes = [False] * n
        visitedNodes[0] = True
        nodeQueue = [0]

        while nodeQueue:
            nextQueue = []
            for currentNode in nodeQueue:
                for nextNode, edgeCost in adjList[currentNode]:
                    if not visitedNodes[nextNode]:
                        visitedNodes[nextNode] = True
                        totalReversals += edgeCost
                        nextQueue.append(nextNode)

            nodeQueue = nextQueue

        ansArray = [0] * n
        ansArray[0] = totalReversals
        visitedNodes = [False] * n
        visitedNodes[0] = True
        nodeQueue = [0]

        while nodeQueue:
            nextQueue = []
            for currentNode in nodeQueue:
                for nextNode, edgeCost in adjList[currentNode]:
                    if not visitedNodes[nextNode]:
                        visitedNodes[nextNode] = True
                        if edgeCost == 0:
                            ansArray[nextNode] = ansArray[currentNode] + 1
                        else:
                            ansArray[nextNode] = ansArray[currentNode] - 1
                        nextQueue.append(nextNode)

            nodeQueue = nextQueue


        return ansArray