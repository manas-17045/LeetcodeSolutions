# Leetcode 3575: Maximum Good Subtree Score
# https://leetcode.com/problems/maximum-good-subtree-score/
# Solved on 2nd of December, 2025
import sys
sys.setrecursionlimit(2000)


class Solution:
    def goodSubtreeSum(self, vals: list[int], par: list[int]) -> int:
        """
        Calculates the sum of maximum good subtree scores for all nodes in a tree.

        Args:
            vals: A list of integers representing the values of the nodes.
            par: A list of integers representing the parent of each node. par[i] is the parent of node i.
                 If par[i] is -1, node i is the root.
        Returns:
            The sum of maximum good subtree scores for all nodes, modulo 10^9 + 7.
        """
        n = len(vals)
        children = [[] for _ in range(n)]
        root = -1
        for i, p in enumerate(par):
            if p != -1:
                children[p].append(i)
            else:
                root = i

        nodeMasks = []
        for val in vals:
            mask = 0
            isValid = True
            seen = set()
            for char in str(val):
                if char in seen:
                    isValid = False
                    break
                seen.add(char)
                mask |= (1 << int(char))
            nodeMasks.append(mask if isValid else -1)

        maxScore = [0] * n

        def dfs(u):
            currDp = {0: 0}
            for v in children[u]:
                childDp = dfs(v)
                nextDp = {}
                for mask1, score1 in currDp.items():
                    for mask2, score2 in childDp.items():
                        if (mask1 & mask2) == 0:
                            newMask = mask1 | mask2
                            newScore = score1 + score2
                            if newScore > nextDp.get(newMask, -1):
                                nextDp[newMask] = newScore
                currDp = nextDp

            uMask = nodeMasks[u]
            if uMask != -1:
                updates = []
                for mask, score in currDp.items():
                    if (mask & uMask) == 0:
                        updates.append((mask | uMask, score + vals[u]))
                for mask, score in updates:
                    if score > currDp.get(mask, -1):
                        currDp[mask] = score

            maxScore[u] = max(currDp.values())
            return currDp

        dfs(root)
        return sum(maxScore) % (10 ** 9 + 7)
