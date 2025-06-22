# Leetcode 3435: Frequencies of Shortest Supersequences
# https://leetcode.com/problems/frequencies-of-shortest-supersequences/
# Solved on 21st of June, 2025
import itertools


class Solution:
    _K_INIT = 0
    _K_VISITING = 1
    _K_VISITED = 2

    def supersequence(self, words: list[str]) -> list[list[int]]:
        """
        Calculates the frequencies of shortest supersequences based on a given list of two-character words.

        A supersequence is formed by characters 'a' through 'z'. Each word 'xy' implies a directed edge x -> y.
        The goal is to find the minimum number of characters that need to be "doubled" (i.e., appear twice)
        in the supersequence such that the resulting graph (where doubled characters are effectively skipped)
        contains no cycles.
        """
        finalFrequenciesList = []

        edges = self.getEdges(words)
        nodesList = self.getNodesList(edges)
        nodeToIndexMap = self.getNodeToIndexMap(nodesList)

        numUniqueNodes = len(nodesList)
        adjList = [[] for _ in range(numUniqueNodes)]

        for uCharValue, vCharValue in edges:
            uGraphIndex = nodeToIndexMap[uCharValue]
            vGraphIndex = nodeToIndexMap[vCharValue]
            adjList[uGraphIndex].append(vGraphIndex)

        minNodeIndexSubsets = self.getMinimumNodeIndexSubsets(adjList)

        for nodeIndexSubset in minNodeIndexSubsets:
            currentFreq = [0] * 26
            for charValue in nodesList:
                currentFreq[charValue] += 1

            for nodeIndex in nodeIndexSubset:
                charValueToDouble = nodesList[nodeIndex]
                currentFreq[charValueToDouble] = 2

            finalFrequenciesList.append(currentFreq)

        return finalFrequenciesList

    def getEdges(self, words: list[str]) -> list[tuple[int, int]]:
        edges = []
        for word in words:
            uCharValue = ord(word[0]) - ord('a')
            vCharValue = ord(word[1]) - ord('a')
            edges.append((uCharValue, vCharValue))
        return edges

    def getNodesList(self, edges: list[tuple[int, int]]) -> list[int]:
        nodeValues = set()
        for uCharValue, vCharValue in edges:
            nodeValues.add(uCharValue)
            nodeValues.add(vCharValue)
        return sorted(list(nodeValues))

    def getNodeToIndexMap(self, nodesList: list[int]) -> list[int]:
        nodeToIndex = [-1] * 26
        for i, charValue in enumerate(nodesList):
            nodeToIndex[charValue] = i
        return nodeToIndex

    def hasCycleRecursive(self, currentGraphIndex: int, adjList: list[list[int]], states: list[int], doubledNodeIndices: set[int]) -> bool:
        if states[currentGraphIndex] == Solution._K_VISITING:
            return True
        if states[currentGraphIndex] == Solution._K_VISITED:
            return False

        states[currentGraphIndex] = Solution._K_VISITING

        if currentGraphIndex not in doubledNodeIndices:
            for neighborGraphIndex in adjList[currentGraphIndex]:
                if neighborGraphIndex not in doubledNodeIndices:
                    if self.hasCycleRecursive(neighborGraphIndex, adjList, states, doubledNodeIndices):
                        return True

        states[currentGraphIndex] = Solution._K_VISITED
        return False

    def graphHasCycleWithSkipping(self, adjList: list[list[int]], doubledNodeIndices: set[int]) -> bool:
        numGraphNodes = len(adjList)
        states = [self._K_INIT] * numGraphNodes
        for i in range(numGraphNodes):
            if self.hasCycleRecursive(i, adjList, states, doubledNodeIndices):
                return True
        return False

    def getMinimumNodeIndexSubsets(self, adjList: list[list[int]]) -> list[list[int]]:
        numGraphNodes = len(adjList)
        resultSubsets = []
        for subsetSize in range(numGraphNodes + 1):
            for nodeIndicesCombination in itertools.combinations(range(numGraphNodes), subsetSize):
                doubledNodeIndices = set(nodeIndicesCombination)

                if not self.graphHasCycleWithSkipping(adjList, doubledNodeIndices):
                    resultSubsets.append(list(nodeIndicesCombination))

            if resultSubsets:
                return resultSubsets
        return resultSubsets