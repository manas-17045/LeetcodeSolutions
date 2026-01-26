# Leetcode 3820: Pythagorean Distance Nodes in a Tree
# https://leetcode.com/problems/pythagorean-distance-nodes-in-a-tree/
# Solved on 26th of January, 2026
import collections


class Solution:
    def specialNodes(self, n: int, edges: list[list[int]], x: int, y: int, z: int) -> int:
        """
        Calculates the number of special nodes in a tree where the distances to three given nodes x, y, and z
        satisfy the Pythagorean theorem (a^2 + b^2 = c^2).

        :param n: The number of nodes in the tree.
        :param edges: A list of edges representing the tree structure.
        :param x: The first reference node.
        :param y: The second reference node.
        :param z: The third reference node.
        :return: The count of nodes i such that the distances to x, y, and z form a Pythagorean triple.
        """
        adjacencyList = [[] for _ in range(n)]
        for u, v in edges:
            adjacencyList[u].append(v)
            adjacencyList[v].append(u)

        def getDistances(startNode):
            distances = [-1] * n
            distances[startNode] = 0
            bfsQueue = collections.deque([startNode])

            while bfsQueue:
                currentNode = bfsQueue.popleft()
                for neighborNode in adjacencyList[currentNode]:
                    if distances[neighborNode] == -1:
                        distances[neighborNode] = distances[currentNode] + 1
                        bfsQueue.append(neighborNode)
            return distances

        distX = getDistances(x)
        distY = getDistances(y)
        distZ = getDistances(z)

        specialNodesCount = 0
        for i in range(n):
            currentDistances = [distX[i], distY[i], distZ[i]]
            currentDistances.sort()

            a = currentDistances[0]
            b = currentDistances[1]
            c = currentDistances[2]

            if a * a + b * b == c * c:
                specialNodesCount += 1

        return specialNodesCount