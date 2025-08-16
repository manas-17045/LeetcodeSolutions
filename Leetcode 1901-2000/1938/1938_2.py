# Leetcode 1938: Maximum Genetic Difference Query
# https://leetcode.com/problems/maximum-genetic-difference-query/
# Solved on 16th of August, 2025
import sys
sys.setrecursionlimit(1 << 25)


class TrieNode:
    __slots__ = ('child', 'count')

    def __init__(self):
        self.child = [None, None]  # child[0], child[1]
        self.count = 0  # number of values passing through this node


class BinaryTrie:
    def __init__(self, maxbit: int = 17):
        # maxbit = highest bit index (0-based). With maxbit=17 we support values < 2^18 (~262k).
        self.root = TrieNode()
        self.maxbit = maxbit

    def add(self, num: int, delta: int):
        node = self.root
        node.count += delta
        for k in range(self.maxbit, -1, -1):
            b = (num >> k) & 1
            if node.child[b] is None:
                node.child[b] = TrieNode()
            node = node.child[b]
            node.count += delta

    def max_xor(self, num: int) -> int:
        node = self.root
        if node.count == 0:
            return 0
        res = 0
        for k in range(self.maxbit, -1, -1):
            b = (num >> k) & 1
            want = 1 - b
            # Choose branch that gives 1 in XOR if available
            if node.child[want] is not None and node.child[want].count > 0:
                res |= (1 << k)
                node = node.child[want]
            else:
                node = node.child[b]
        return res


class Solution:
    def maxGeneticDifference(self, parents: list[int], queries: list[list[int]]) -> list[int]:
        """
        Calculates the maximum genetic difference (XOR sum) for a set of queries
        on a tree structure defined by parent-child relationships.

        Args:
            parents: A list where parents[i] is the parent of node i. -1 indicates the root.
            queries: A list of queries, where each query is [node, val].

        Returns:
            A list of integers, where ans[i] is the maximum XOR sum for queries[i].
        """
        n = len(parents)
        # Build children adjacency
        children = [[] for _ in range(n)]
        root = -1
        for i, p in enumerate(parents):
            if p == -1:
                root = i
            else:
                children[p].append(i)

        # Group queries by node: node -> list of (val, query_index)
        q_by_node = [[] for _ in range(n)]
        for i, (node, val) in enumerate(queries):
            q_by_node[node].append((val, i))

        ans = [0] * len(queries)
        trie = BinaryTrie(maxbit=17)  # values <= 2*10^5, 18 bits suffice

        def dfs(u: int):
            # Add current node's genetic value (which equals its index)
            trie.add(u, 1)
            # Answer queries attached to this node
            for val, qi in q_by_node[u]:
                ans[qi] = trie.max_xor(val)
            # Recurse
            for v in children[u]:
                dfs(v)
            # Remove current node's value when backtracking
            trie.add(u, -1)

        # Start DFS from root
        if root != -1:
            dfs(root)
        return ans
