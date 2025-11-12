# Leetcode 2612: Minimum Reverse Operations
# https://leetcode.com/problems/minimum-reverse-operations/
# Solved on 12th of November, 2025
import collections


class Solution:
    def minReverseOperations(self, n: int, p: int, banned: list[int], k: int) -> list[int]:
        """
        Calculates the minimum number of reverse operations to reach each index from a starting index p,
        avoiding banned indices.

        Args:
            n (int): The total number of indices (0 to n-1).
            p (int): The starting index.
            banned (list[int]): A list of banned indices.
            k (int): The length of the subarray to reverse.

        Returns:
            list[int]: An array where answer[i] is the minimum number of operations to reach index i, or -1 if unreachable.
        """

        parent = list(range(n + 2))

        def find(i):
            if i >= n:
                return i
            path = []
            while i != parent[i]:
                path.append(i)
                i = parent[i]
                if i >= n:
                    break

            root = i
            for node in path:
                parent[node] = root
            return root

        answer = [-1] * n
        bannedSet = set(banned)

        for b in bannedSet:
            if b < n:
                parent[b] = find(b + 2)

        if p in bannedSet:
            return answer

        answer[p] = 0
        parent[p] = find(p + 2)

        queue = collections.deque([p])

        while queue:
            curr = queue.popleft()
            dist = answer[curr]

            minL = max(0, curr - k + 1)
            maxL = min(curr, n - k)

            if minL > maxL:
                continue

            minJ = 2 * minL + k - 1 - curr
            maxJ = 2 * maxL + k - 1 - curr

            targetParity = (curr + k - 1) % 2

            startJ = minJ
            if startJ % 2 != targetParity:
                startJ += 1

            if startJ > maxJ:
                continue

            currJ = find(startJ)

            while currJ <= maxJ:
                answer[currJ] = dist + 1
                queue.append(currJ)

                parent[currJ] = find(currJ + 2)

                currJ = parent[currJ]

        return answer