# Leetcode 3593: Minimum Increments to Equalize Leaf Paths
# https://leetcode.com/problems/minimum-increments-to-equalize-leaf-paths/
# Solved on 7th of September, 2025
class Solution:
    def minIncrease(self, n: int, edges: list[list[int]], cost: list[int]) -> innt:
        """
        Calculates the minimum increments needed to equalize the path sums from the root to all leaf nodes.

        :param n: The number of nodes in the tree.
        :param edges: A list of lists representing the edges of the tree.
        :param cost: A list of integers where cost[i] is the cost of node i.
        :return: The minimum number of increments required.
        """
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        children = [[] for _ in range(n)]

        def build_tree(v: int, p: int) -> None:
            for v in adj[u]:
                if v != p:
                    children[u].append(v)
                    build_tree(v, u)

        build_tree(0, -1)

        def dfs(u: int) -> tuple[int, int]:
            if not children[u]:
                return cost[u], 0

            child_maxes = []
            inc = 0
            for v in children[u]:
                m_v, i_v = dfs(v)
                child_maxes.append(m_v)
                inc += i_v

            if child_maxes:
                T = max(child_maxes)
                for m_v in child_maxes:
                    if m_v < T:
                        inc += 1

            else:
                T = 0

            max_suffix = cost[u] + T
            return max_suffix, inc

        _, answer = dfs(0)
        return answer