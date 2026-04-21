# Leetcode 1722: Minimize Hamming Distance After Swap Operations
# https://leetcode.com/problems/minimize-hamming-distance-after-swap-operations/
# Solved on 21st of April, 2026
from collections import defaultdict, Counter


class Solution:
    def minimumHammingDistance(self, source: list[int], target: list[int], allowedSwaps: list[list[int]]) -> int:
        """
        Calculates the minimum Hamming distance between source and target arrays after any number of allowed swaps.

        :param source: The initial list of integers.
        :param target: The target list of integers to compare against.
        :param allowedSwaps: A list of index pairs that can be swapped in the source array.
        :return: The minimum possible Hamming distance between the modified source and the target.
        """
        arrayLength = len(source)
        parentArray = list(range(arrayLength))
        rankArray = [1] * arrayLength

        def findRoot(nodeId):
            if parentArray[nodeId] != nodeId:
                parentArray[nodeId] = findRoot(parentArray[nodeId])
            return parentArray[nodeId]

        def unionNodes(nodeA, nodeB):
            rootA = findRoot(nodeA)
            rootB = findRoot(nodeB)
            if rootA != rootB:
                if rankArray[rootA] > rankArray[rootB]:
                    parentArray[rootB] = rootA
                elif rankArray[rootA] < rankArray[rootB]:
                    parentArray[rootA] = rootB
                else:
                    parentArray[rootB] = rootA
                    rankArray[rootA] += 1

        for swapPair in allowedSwaps:
            unionNodes(swapPair[0], swapPair[1])

        elementCountMap = defaultdict(Counter)

        for currIndex in range(arrayLength):
            rootIndex = findRoot(currIndex)
            elementCountMap[rootIndex][source[currIndex]] += 1

        minDistance = 0

        for currIndex in range(arrayLength):
            rootIndex = findRoot(currIndex)
            targetValue = target[currIndex]
            if elementCountMap[rootIndex][targetValue] > 0:
                elementCountMap[rootIndex][targetValue] -= 1
            else:
                minDistance += 1

        return minDistance