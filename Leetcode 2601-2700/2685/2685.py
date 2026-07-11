# Leetcode 2685: Count the Number of Complete Components
# https://leetcode.com/problems/count-the-number-of-complete-components/
# Solved on 11th of July, 2026
class Solution:
    def countCompleteComponents(self, n: int, edges: list[list[int]]) -> int:
        """
        Counts the number of complete components in a graph.

        Args:
            n: The number of nodes in the graph.
            edges: The edges in the graph.

        Returns:
            The number of complete components.
        """
        adjList = [[] for _ in range(n)]
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
        
        visitedNodes = [False] * n
        completeComponentCount = 0

        for i in range(n):
            if not visitedNodes[i]:
                componentNodes = []
                nodeStack = []
                visitedNodes[i] = True

                while nodeStack:
                    currentNode = nodeStack.pop()
                    componentNodes.append(currentNode)
                    for neighborNode in adjList[currentNode]:
                        if not visitedNodes[neighborNode]:
                            visitedNodes[neighborNode] = True
                            nodeStack.append(neighborNode)
                
                nodeCount = len(componentNodes)
                isComplete = True
                for node in componentNodes:
                    if len(adjList[node]) != nodeCount - 1:
                        isComplete = False
                        break
                
                if isComplete:
                    completeComponentCount += 1
        
        return completeComponentCount