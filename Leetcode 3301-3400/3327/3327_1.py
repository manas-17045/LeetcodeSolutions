# Leetcode 3327: Check if DFS Strings Are Palindromes
# https://leetcode.com/problems/check-if-dfs-strings-are-palindromes/
# Solved on 26th of May, 2025
import sys


class Solution:
    def findAnswer(self, parent: list[int], s: str) -> list[bool]:
        """
        Finds for each node u, whether the string S_u formed by concatenating
        the characters s[v] for all nodes v in the subtree of u (including u),
        sorted by their node IDs, is a palindrome.

        Args:
            parent: A list where parent[i] is the parent of node i for i > 0,
                    and parent[0] is -1 (root). Represents a valid tree.
            s: A string of length n, where s[i] is the character at node i.

        Returns:
            A list of booleans of length n, where the i-th element is true if S_i is a palindrome.
        """
        n = len(parent)
        adj = [[] for _ in range(n)]
        # parent[0] is -1. Node 0 is the root.
        # For i from 1 to (n - 1), parent[i] is the parent of node i.
        for i in range(1, n):
            # Problem statement guarantees parent represents a valid tree.
            adj[parent[i]].append(i)

        # Children in adj[u] are added in increasing order of their IDs
        # because the loop `for i in range(1, n)` processes node IDs in increasing order.

        # Hashing parameters
        P1, M1 = 31, 10**9 + 7
        P2, M2 = 53, 10**9 + 9

        # Precompute powers of P1, P2 modulo M1, M2
        # p_powers[k] = P^k. Max k needed is n (for p_powers[n-1] or p_powers[n] depending on indexing).
        # Size n+1 for p_powers array (indices 0 to n) is safe.
        p_powers1 = [1] * (n + 1)
        p_powers2 = [1] * (n + 1)
        for i in range(1, n + 1):   # Loop from 1 to n inclusive
            p_powers1[i] = (p_powers1[i - 1] * P1) % M1
            p_powers2[i] = (p_powers2[i - 1] * P2) % M2

        # Precompute powers of P1, P2 modulo M1, M2
        # p_powers[k] = p^k. Max k is n (for p_powers[n - 1] or p_powers[n] depending on indexing).
        # Size n+1 for p_powers array (indices 0 to n) is safe.
        p_powers1 = [1] * (n + 1)
        p_powers2 = [1] * (n + 1)
        for i in range(1, n + 1):   # Loop from 1 to n inclusive
            p_powers1[i] = (p_powers1[i - 1] * P1) % M1
            p_powers2[i] = (p_powers2[i - 1] * P2) % M2

        # Arrays to store results for each node u
        h1_values = [0] * n     # Forward hash for S_u with (P1, M1)
        hr1_values = [0] * n    # Reverse hash for S_u with (P1, M1)
        h2_values = [0] * n     # Forward hash for S_u with (P2, M2)
        hr2_values = [0] * n    # Reverse hash for S_u with (P2, M2)
        subtree_len = [0] * n   # Length of S_u (size of subtree rooted at u)

        answer = [False] * n    # answer[u] is true if S_u is a palindrome

        # Adjust Python's recursion limit for deep trees. Max depth can be n.
        required_recursion_limit = n + 50   # Add a small buffer
        try:
            current_recursion_limit = sys.getrecursionlimit()
            if required_recursion_limit > current_recursion_limit:
                sys.setrecursionlimit(required_recursion_limit)
        except RuntimeError:
            # Some environments might restrict changing recursion limit
            # This solution assumes it's possible or the default limit is enough.
            pass

        # DFS function to compute hashes and check palindrome.
        # This is a post-order traversal" process children, then process the node.
        def computeHashesDFS(u: int):
            # Aggregate hashes and length for the string formed by concatenating S_child of children of u.
            # This is S_children_combined = S_c1 + S_c2 + ... + S_ck
            current_h1 = 0      # h(S_children_combined) with (P1, M1)
            current_hr1 = 0     # hr(S_children_combined) with (P1, M1)
            current_h2 = 0      # h(S_children_combined) with (P2, M2)
            current_hr2 = 0     # hr(S_children_combined) with (P2, M2)
            current_len = 0     # len(S_children_combined)

            # Iterate over children of u (they are sorted by ID in adj[u])
            for v_child in adj[u]:
                computeHashesDFS(v_child)   # Recursive call for child

                # Child's values (h*(S_{v_child}), hr*(S_{v_child}), len(S_{v_child}))
                # are now computed and stored in the global-like arrays.

                # Let A = S_children_combined (string from already processed children of u)
                # Let B = S_{v_child} (string from the current child v_child)
                # New S_children_combined becomes A + B

                # Hash 1 update:
                # h(A+B) = (h(A) * P1^len(B) + h(B))
                current_h1 = (current_h1 * p_powers1[subtree_len[v_child]] + h1_values[v_child]) % M1
                # hr(A+B) = (hr(B) * P1^len(A) + hr(A))
                current_hr1 = (hr1_values[v_child] * p_powers1[current_len] + current_hr1) % M1

                # Hash 2 update:
                current_h2 = (current_h2 * p_powers2[subtree_len[v_child]] + h2_values[v_child]) % M2
                current_hr2 = (hr2_values[v_child] * p_powers2[current_len] + current_hr2) % M2

                current_len += subtree_len[v_child]

            # All children processed.
            # (current_h*, current_hr*, current_len) now represent S_children_combined for node u.
            # Now, form S_u = S_children_combined + s[u].
            char_val = ord(s[u]) - ord('a') + 1     # Map 'a' -> 1, 'b' -> 2, ..., 'z' -> 26

            # Finalize hashes for S_u
            # Let C = S_children_combined, char = s[u] (a single character, length 1)
            # S_u = C + char

            # Hash 1 for S_u:
            # h(C + char) = (h(C) * P1^1 + val(char))
            h1_values[u] = (current_h1 * p_powers1[1] + char_val) % M1
            # hr(C + char) = (hr(C) * P1^len(C) + val(char))
            hr1_values[u] = (current_hr1 * p_powers1[current_len] + char_val) % M1

            # Hash 2 for S_u:
            h2_values[u] = (current_h2 * p_powers2[1] + char_val) % M2
            hr2_values[u] = (current_hr2 * p_powers2[current_len] + char_val) % M2

            subtree_len[u] = current_len + 1

            # Check if S_u is a palindrome
            if h1_values[u] == hr1_values[u] and h2_values[u] == hr2_values[u]:
                answer[u] = True

        # Constraints: 1 <= n. Node 0 is the root of the tree.
        # Start DFS from node 0, which will cover all nodes in the tree.
        if n > 0:   # Should always be true based on constraints (n >= 1)
            computeHashesDFS(0)

        return answer