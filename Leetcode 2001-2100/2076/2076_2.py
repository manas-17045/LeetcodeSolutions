# Leetcode 2076: Process Restricted Friend Requests
# https://leetcode.com/problems/process-restricted-friend-requests/
# Solved on 26th of May, 2025

class Solution:
    def friendRequests(self, n: int, restrictions: list[list[int]], requests: list[list[int]]) -> list[bool]:
        """
        Determines which friend requests can be accepted given a set of restrictions.

        Args:
            n: The number of people.
            restrictions: A list of pairs of people who cannot be friends.
            requests: A list of friend requests.

        Returns:
            A list of booleans indicating whether each request can be accepted.
        """
        parent = list(range(n))
        rank = [0] * n

        def find(x: int) -> int:
            # Path compression
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a: int, b: int) -> None:
            ra, rb = find(a), find(b)
            if ra == rb:
                return
            # Union by Rank
            if rank[ra] < rank[rb]:
                parent[rb] = ra
            elif rank[rb] < rank[ra]:
                parent[ra] = rb
            else:
                parent[rb] = ra
                rank[ra] += 1

        ans = []
        for u, v in requests:
            ru, rv = find(u), find(v)
            # Already in same group -> always accept
            if ru == rv:
                ans.append(True)
                continue

            # Check every restriction
            violation = False
            for x, y in restrictions:
                rx, ry = find(x), find(y)
                # If a restriction paor would end up in same group after union(ru, rv)
                if (rx == ru and ry == rv) or (rx == rv and ry == ru):
                    violation = True
                    break

            if violation:
                ans.append(False)
            else:
                # Safe to merge
                union(ru, rv)
                ans.append(True)

        return ans