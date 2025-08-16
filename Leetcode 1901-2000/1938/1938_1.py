# Leetcode 1938: Maximum Genetic Difference Query
# https://leetcode.com/problems/maximum-genetic-difference-query/
# Solved on 16th of August, 2025
class Solution:
    def maxGeneticDifference(self, parents: list[int], queries: list[list[int]]) -> list[int]:
        """
        Calculates the maximum genetic difference for a series of queries.

        Args:
            parents: A list representing the parent of each node. parents[i] is the parent of node i.
            queries: A list of queries, where each query is [node, val].
        Returns:
            A list of integers, where the i-th element is the maximum genetic difference for the i-th query.
        """
        MAX_BITS = 18

        class BinaryTrie:
            def __init__(self):
                self.root = {'children': {}, 'count': 0}

            def insert(self, value):
                trieNode = self.root
                trieNode['count'] += 1
                for bitPosition in range(MAX_BITS - 1, -1, -1):
                    bit = (value >> bitPosition) & 1
                    if bit not in trieNode['children']:
                        trieNode['children'][bit] = {'children': {}, 'count': 0}
                    trieNode = trieNode['children'][bit]
                    trieNode['count'] += 1

            def remove(self, value):
                trieNode = self.root
                trieNode['count'] -= 1
                for bitPosition in range(MAX_BITS - 1, -1, -1):
                    bit = (value >> bitPosition) & 1
                    trieNode = trieNode['children'][bit]
                    trieNode['count'] -= 1

            def findMaxXor(self, value):
                if self.root['count'] == 0:
                    return -1

                trieNode = self.root
                maxResult = 0
                for bitPosition in range(MAX_BITS - 1, -1, -1):
                    bit = (value >> bitPosition) & 1
                    oppositeBit = 1 - bit

                    if oppositeBit in trieNode['children'] and trieNode['children'][oppositeBit]['count'] > 0:
                        maxResult |= (1 << bitPosition)
                        trieNode = trieNode['children'][oppositeBit]
                    else:
                        trieNode = trieNode['children'][bit]
                return maxResult

        numNodes = len(parents)
        adjacencyList = [[] for _ in range(numNodes)]
        rootNode = -1
        for nodeIndex, parentNode in enumerate(parents):
            if parentNode == -1:
                rootNode = nodeIndex
            else:
                adjacencyList[parentNode].append(nodeIndex)

        queriesByNode = [[] for _ in range(numNodes)]
        for queryIndex, query in enumerate(queries):
            node, value = query
            queriesByNode[node].append((value, queryIndex))

        answerList = [0] * len(queries)
        trie = BinaryTrie()

        def dfs(currentNode):
            trie.insert(currentNode)

            for queryValue, queryIndex in queriesByNode[currentNode]:
                answerList[queryIndex] = trie.findMaxXor(queryValue)

            for childNode in adjacencyList[currentNode]:
                dfs(childNode)

            trie.remove(currentNode)

        if rootNode != -1:
            dfs(rootNode)

        return answerList