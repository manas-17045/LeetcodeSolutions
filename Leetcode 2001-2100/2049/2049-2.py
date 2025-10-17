# Leetcode 2049: Count Nodes With The Highest Score
# https://leetcode.com/problems/count-nodes-with-the-highest-score/
# Solved on 17th of October, 2025
class Solution:
    def countHighestScoreNodes(self, parents: list[int]) -> int:
        """
        Counts the number of nodes that have the highest possible score when removed.
        The score of a node is calculated by multiplying the sizes of the subtrees
        formed by removing that node.
        :param parents: A list where parents[i] is the parent of node i. parents[0] is -1.
        :return: The number of nodes that achieve the maximum score.
        """
        n = len(parents)
        # Build children lists
        children = [[] for _ in range(n)]
        root = -1
        for i, p in enumerate(parents):
            if p == -1:
                root = i
            else:
                children[p].append(i)

        # Iterative post-order DFS to compute subtree sizes
        size = [0] * n
        stack = [(root, False)]
        while stack:
            node, visited = stack.pop()
            if not visited:
                stack.append((node, True))
                for c in children[node]:
                    stack.append((c, False))
            else:
                s = 1
                for c in children[node]:
                    s += size[c]
                size[node] = s

        # Compute scores and count max
        max_score = 0
        count = 0

        for i in range(n):
            score = 1
            # Product of child subtree sizes
            for c in children[i]:
                score *= size[c]
            # Size of remaining (parent-size) component
            rem = n - size[i]
            if rem > 0:
                score *= rem

            if score > max_score:
                max_score = score
                count = 1
            elif score == max_score:
                count += 1

        return count