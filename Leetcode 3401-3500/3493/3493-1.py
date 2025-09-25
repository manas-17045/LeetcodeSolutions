# Leetcode 3493: Properties Graph
# https://leetcode.com/problems/properties-graph/
# Solved on 25th of September, 2025
class Solution:
    def numberOfComponents(self, properties: list[list[int]], k: int) -> int:
        """
        Calculates the number of connected components in a graph where nodes are properties
        and an edge exists between two properties if they share at least 'k' common elements.
        :param properties: A list of lists, where each inner list represents a set of properties.
        :param k: The minimum number of common elements required to form an edge between two properties.
        :return: The total number of connected components in the graph.
        """
        numProperties = len(properties)

        parent = list(range(numProperties))
        size = [1] * numProperties
        componentCount = numProperties

        def find(nodeIndex):
            if parent[nodeIndex] == nodeIndex:
                return nodeIndex
            parent[nodeIndex] = find(parent[nodeIndex])
            return parent[nodeIndex]

        def union(indexOne, indexTwo):
            nonlocal componentCount
            rootOne = find(indexOne)
            rootTwo = find(indexTwo)

            if rootOne != rootTwo:
                if size[rootOne] < size[rootTwo]:
                    rootOne, rootTwo = rootTwo, rootOne

                parent[rootTwo] = rootOne
                size[rootOne] += size[rootTwo]
                componentCount -= 1

        propertySets = [set(p) for p in properties]

        for i in range(numProperties):
            for j in range(i + 1, numProperties):
                setOne = propertySets[i]
                setTwo = propertySets[j]

                intersectionSize = len(setOne.intersection(setTwo))

                if intersectionSize >= k:
                    union(i, j)

        return componentCount