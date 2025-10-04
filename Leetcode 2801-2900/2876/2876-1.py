# Leetcode 2876: Count Visited Nodes in a Directed Graph
# https://leetcode.com/problems/count-visited-nodes-in-a-directed-graph/
# Solved on 4th of October, 2025
import collections


class Solution:
    def countVisitedNodes(self, edges: list[int]) -> list[int]:
        """
        Counts the number of nodes reachable from each node in a directed graph.

        :param edges: A list where edges[i] is the node that node i points to.
        :return: A list where answer[i] is the number of nodes reachable from node i.
        """
        n = len(edges)
        answer = [0] * n
        inDegree = [0] * n
        for destinationNode in edges:
            inDegree[destinationNode] += 1

        queue = collections.deque()
        for i in range(n):
            if inDegree[i] == 0:
                queue.append(i)

        tailNodes = []
        while queue:
            currentNode = queue.popleft()
            tailNodes.append(currentNode)

            nextNode = edges[currentNode]
            inDegree[nextNode] -= 1
            if inDegree[nextNode] == 0:
                queue.append(nextNode)

        for i in range(n):
            if inDegree[i] > 0 and answer[i] == 0:
                cycleNodes = [i]
                currentNode = edges[i]
                while currentNode != i:
                    cycleNodes.append(currentNode)
                    currentNode = edges[currentNode]

                cycleLength = len(cycleNodes)
                for node in cycleNodes:
                    answer[node] = cycleLength

        for node in reversed(tailNodes):
            nextNode = edges[node]
            answer[node] = answer[nextNode] + 1

        return answer