# Leetcode 839: Similar String Groups
# https://leetcode.com/problems/similar-string-groups/
# Solved on 9th of July, 2025
class Solution:
    def numSimilarGroups(self, strs: list[str]) -> int:
        """
        Given a list of strings `strs`, return the number of groups of similar strings.

        Two strings `X` and `Y` are similar if we can swap two letters (in different positions) of `X`
        to make it equal to `Y`. Also, `X` and `Y` are similar if they are already equal.

        This problem can be solved using a Disjoint Set Union (DSU) data structure.
        Each string initially forms its own group. We then iterate through all pairs of strings,
        and if two strings are similar, we union their respective groups. Finally, the number of
        distinct groups (roots in the DSU) is the answer.
        """
        n = len(strs)

        # DSU / Union-Find setup
        parent = list(range(n))
        rank = [0] * n

        def find(x: int) -> int:
            """Path-compressed find"""
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a: int, b: int) -> None:
            """Union by rank"""
            ra, rb = find(a), find(b)
            if ra == rb:
                return
            if rank[ra] < rank[rb]:
                parent[ra] = rb
            elif rank[ra] > rank[rb]:
                parent[rb] = ra
            else:
                parent[rb] = ra
                rank[ra] += 1

        def is_similar(a: str, b: str) -> bool:
            diff = 0
            for ca, cb in zip(a, b):
                if ca != cb:
                    diff += 1
                    if diff > 2:
                        return False
            return True

        # Merge all similar pairs
        for i in range(n):
            for j in range((i + 1), n):
                # Only union if not already in the same group
                if find(i) != find(j) and is_similar(strs[i], strs[j]):
                    union(i, j)

        # Count distinct roots
        roots = {find(i) for i in range(n)}
        return len(roots)