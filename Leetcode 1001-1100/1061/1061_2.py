# Leetcode 1061: Lexicographically Smallest Equivalent String
# https://leetcode.com/problems/lexicographically-smallest-equivalent-string/
# Solved on 5th of June, 2025

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        """
        Given two strings s1 and s2 of equal length, we define a string s3 to be equivalent to s4 if,
        at every index i, s3[i] and s4[i] are equivalent characters.
        Two characters a and b are equivalent if:
        - a == b, or
        - a is equivalent to c, and c is equivalent to b for some character c.

        Return the lexicographically smallest string that is equivalent to baseStr.

        This solution uses a Union-Find data structure to group equivalent characters.
        The representative of each group is the lexicographically smallest character in that group.
        """
        # Union-Find (Disjoint Set Union) data structure over 26 lowercase letters.
        parent = list(range(26))

        def find(x: int) -> int:
            # Path compression
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x: int, y: int) -> None:
            # Merge the sets, always attaching the larger-index root to the smaller-index root
            rootX = find(x)
            rootY = find(y)
            if rootX == rootY:
                return
            if rootX < rootY:
                parent[rootY] = rootX
            else:
                parent[rootX] = rootY

        # Build equivalences from s1 and s2
        for c1, c2 in zip(s1, s2):
            i1 = ord(c1) - ord('a')
            i2 = ord(c2) - ord('a')
            union(i1, i2)

        # For each character, find its lexicographically smallest representative and build the resulting string.
        result = []
        for c in baseStr:
            idx = ord(c) - ord('a')
            root = find(idx)
            smallestChar = chr(root + ord('a'))
            result.append(smallestChar)

        return "".join(result)