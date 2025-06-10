# Leetcode 2867: Count Valid Paths in a Tree
# https://leetcode.com/problems/count-valid-paths-in-a-tree/
# Solved on 10th of June, 2025

class Solution:
    def countPaths(self, n: int, edges: list[list[int]]) -> int:
        # Sieve primes up to n
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(n**0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, n + 1, i):
                    is_prime[j] = False

        # Build adjacency
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # Find non-prime components
        comp_id = [0] * (n + 1)
        comp_size = []
        curr_comp = 0

        for node in range(1, (n + 1)):
            if not is_prime[node] and comp_id[node] == 0:
                curr_comp += 1
                size = 0
                stack = [node]
                comp_id[node] = curr_comp
                while stack:
                    u = stack.pop()
                    size += 1
                    for w in adj[u]:
                        if (not is_prime[w]) and comp_id[w] == 0:
                            comp_id[w] = curr_comp
                            stack.append(w)
                # comp_size[curr_comp - 1] = size
                comp_size.append(size)

        # For each prime, gather ts adjacent non-prime components
        ans = 0
        for p in range(1, (n + 1)):
            if not is_prime[p]:
                continue
            sum_sz = 0
            sum_sq =0
            # Look at each neighbor of p
            for q in adj[p]:
                if not is_prime[q]:
                    cid = comp_id[q] - 1
                    s = comp_size[cid]
                    sum_sz += s
                    sum_sq += s * s
            # Pairs (one endpoint = p, other non-prime): sum_sz
            # Pairs (two non-prime ends in different subtrees): ((sum_sz^2 - sum_sq) // 2)
            ans += sum_sz + (sum_sz * sum_sz - sum_sq) // 2

        return ans