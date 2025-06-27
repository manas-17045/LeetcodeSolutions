# Leetcode 2246: Longest Path With Different Adjacent Characters
# https://leetcode.com/problems/longest-path-with-different-adjacent-characters/
# Solved on 27th of June, 2025
class Solution:
    def longestPath(self, parent: list[int], s: str) -> int:
        """
        Calculates the longest path in a tree such that no two adjacent nodes
        on the path have the same character.

        Args:
            parent: A list representing the parent of each node. parent[i] is the parent of node i.
                    parent[0] is always -1, indicating the root.
            s: A string where s[i] is the character of node i.
        Returns:
            The length of the longest path with different adjacent characters.
        """
        numNodes = len(parent)
        adjacencyList = [[] for _ in range(numNodes)]
        for i in range(1, numNodes):
            adjacencyList[parent[i]].append(i)

        self.maxLength = 0

        def dfs(currentNode):
            longestChain = 0
            secondLongestChain = 0

            for childNode in adjacencyList[currentNode]:
                pathFromChild = dfs(childNode)
                if s[currentNode] != s[childNode]:
                    if pathFromChild > longestChain:
                        secondLongestChain = longestChain
                        longestChain = pathFromChild
                    elif pathFromChild > secondLongestChain:
                        secondLongestChain = pathFromChild

            self.maxLength = max(self.maxLength, longestChain + secondLongestChain + 1)

            return 1 + longestChain

        dfs(0)
        return self.maxLength