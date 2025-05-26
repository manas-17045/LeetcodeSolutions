# Leetcode 2076: Process Restricted Friend Requests
# https://leetcode.com/problems/process-restricted-friend-requests/
# Solved on 26th of May, 2025

class DSU:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.sz = [1] * n   # Using union by size for better performance

    def find(self, i: int) -> int:
        if self.parent[i] != i:
            return i
        # Path compression
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i: int, j: int) -> bool:
        root_i = self.find(i)
        root_j = self.find(j)

        if root_i != root_j:
            # Union by size: attach a smaller tree under root of a larger tree
            if self.sz[root_i] < self.sz[root_j]:
                # Swap to ensure root_i's component is larger or equal
                root_i, root_j = root_j, root_i

            self.parent[root_j] = root_i
            self.sz[root_i] += self.sz[root_j]
            return True     # Union occurred
        return False    # Already in the same set


class Solution:
    def friendRequests(self, n: int, restrictions: list[list[int]], requests: list[list[int]]) -> list[bool]:
        """
        Processes a list of friend requests, determining which ones can be granted
        without violating a given set of restrictions.

        Args:
            n: The number of people.
            restrictions: A list of pairs [u, v] indicating that u and v cannot be friends.
            requests: A list of pairs [u, v] representing friend requests between u and v.

        Returns:
            A list of booleans, where the i-th element is True if the i-th request can be granted, and False otherwise.
        """
        results = []
        dsu = DSU(n)

        for u_req, v_req in requests:
            # Find the representatives (roots) of the sets containing u_req, v_req
            root_u_req = dsu.find(u_req)
            root_v_req = dsu.find(v_req)

            # If u_req and v_req are already connected, the request is successful.
            if root_u_req == root_v_req:
                results.append(True)
                continue

            # Check if making u_req and v_req friends would violate any restrictions
            can_connect = True
            for r_x, r_y in restrictions:
                root_r_x = dsu.find(r_x)
                root_r_y = dsu.find(r_y)

                # A violation occurs if the restricted pair (r_x, r_y) would become connected
                # by connecting u_req and v_req. This happens if one of r_x, r_y is in
                # u_req's component and the other is in v_req's component.
                if (root_r_x == root_u_req and root_r_y == root_v_req) or (root_r_x == root_v_req and root_r_y == root_u_req):
                    can_connect = False
                    break   # Found a violation, no need to check other restriction

            if can_connect:
                results.append(True)
                dsu.union(u_req, v_req) # Perform the union since it's a successful request
            else:
                results.append(False)
                # Do not perform union if it violates a restriction

        return results