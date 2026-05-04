# Leetcode 3910: Count Connected Subgraphs with Even Node Sum
# https://leetcode.com/problems/count-connected-subgraphs-with-even-node-sum/
# Solved on 4th of May, 2026
class Solution:
    def evenSumSubgraphs(self, nums: list[int], edges: list[list[int]]) -> int:
        """
        Counts the number of connected subgraphs where the sum of node values is even.

        :param nums: A list of integers representing the values of each node.
        :param edges: A list of pairs representing the undirected edges of the graph.
        :return: The total count of connected subgraphs with an even sum.
        """
        nodeCount = len(nums)
        adjacencyMap = [0] * nodeCount

        for edge in edges:
            nodeU = edge[0]
            nodeV = edge[1]
            adjacencyMap[nodeU] |= (1 << nodeV)
            adjacencyMap[nodeV] |= (1 << nodeU)

        validSubgraphsCount = 0

        for mask in range(1, 1 << nodeCount):
            currentParity = 0
            firstNode = -1
            tempMask = mask

            while tempMask > 0:
                nodeIndex = (tempMask & -tempMask).bit_length() - 1
                currentParity ^= nums[nodeIndex]
                if firstNode == -1:
                    firstNode = nodeIndex
                tempMask &= tempMask - 1

            if currentParity == 1:
                continue

            visitedMask = 1 << firstNode
            dfsStack = [firstNode]

            while dfsStack:
                currentNode = dfsStack.pop()
                validNeighbors = adjacencyMap[currentNode] & mask
                unvisitedNeighbors = validNeighbors & ~visitedMask

                while unvisitedNeighbors > 0:
                    neighborIndex = (unvisitedNeighbors & -unvisitedNeighbors).bit_length() - 1
                    visitedMask |= (1 << neighborIndex)
                    dfsStack.append(neighborIndex)
                    unvisitedNeighbors &= unvisitedNeighbors - 1

            if visitedMask == mask:
                validSubgraphsCount += 1

        return validSubgraphsCount