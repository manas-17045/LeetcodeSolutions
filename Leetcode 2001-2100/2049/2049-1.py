# Leetcode 2049: Count Nodes With The Highest Score
# https://leetcode.com/problems/count-nodes-with-the-highest-score/
# Solved on 17th of October, 2025
class Solution:
    def countHighestScoreNodes(self, parents: list[int]) -> int:
        """
        Counts the number of nodes that have the highest score.

        A node's score is calculated by multiplying the sizes of the components
        formed by removing that node.
        :param parents: A list where parents[i] is the parent of node i. parents[0] is -1.
        :return: The number of nodes with the highest score.
        """
        n = len(parents)
        adjList = [[] for _ in range(n)]
        for i, p in enumerate(parents):
            if p != -1:
                adjList[p].append(i)

        scoreInfo = [0, 0]

        def dfs(node):
            subtreeSize = 1
            currentScore = 1

            for child in adjList[node]:
                childSubtreeSize = dfs(child)
                subtreeSize += childSubtreeSize
                currentScore *= childSubtreeSize

            parentComponentSize = n - subtreeSize
            if parentComponentSize > 0:
                currentScore *= parentComponentSize

            if currentScore > scoreInfo[0]:
                scoreInfo[0] = currentScore
                scoreInfo[1] = 1
            elif currentScore == scoreInfo[0]:
                scoreInfo[1] += 1

            return subtreeSize

        dfs(0)
        return scoreInfo[1]