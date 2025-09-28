# Leetcode 1916: Count Ways to Build Rooms in an Ant Colony
# https://leeetcode.com/problems/count-ways-to-build-rooms-in-an-ant-colony/
# Solved on 27th of September, 2025
class Solution:
    def waysToBuildRooms(self, prevRoom: list[int]) -> int:
        """
        Calculates the number of ways to build rooms such that the given `prevRoom`
        relationships are maintained.

        :param prevRoom: A list where prevRoom[i] is the parent of room i. prevRoom[0] is -1.
        :return: The number of ways to build the rooms modulo 10^9 + 7.
        """
        MOD = 10**9 + 7
        n = len(prevRoom)

        # Build children lists
        children = [[] for _ in range(n)]
        for i in range (1, n):
            p = prevRoom[i]
            children[p].append(i)

        # Precompute factorials and inverse factorials
        fact = [1] * (n + 1)
        for i in range(1, n + 1):
            fact[i] = (fact[i - 1] * i) % MOD
        invFact = [1] * (n + 1)
        invFact[n] = pow(fact[n], MOD - 2, MOD)
        for i in range(n, 0, -1):
            invFact[i - 1] = (invFact[i] * i) % MOD

        def comb(a: int, b: int) -> int:
            if b < 0 or b > a:
                return 0
            return fact[a] * invFact[b] % MOD * invFact[a - b] % MOD

        # Iterative postorder traversal to get nodes in postorder
        stack = [0]
        order = []
        while stack:
            u = stack.pop()
            order.append(u)
            for v in children[u]:
                stack.append(v)

        # Order currently is preorder-like; reverse to get postorder
        order.reverse()

        subtree_size = [0] * n
        ways = [0] * n

        for u in order:
            total = 0
            w = 1
            for c in children[u]:
                # Multiply by child's internal ways
                w = (w * ways[c]) % MOD
                # Multiply by comb(total + size_c, size_c) to interleave child's nodes
                w = (w * comb(total + subtree_size[c], subtree_size[c])) % MOD
                total += subtree_size[c]
            subtree_size[u] = total + 1
            ways[u] = w % MOD

        return ways[0] % MOD