# Leetcode 1345: Jump Game IV
# https://leetcode.com/problems/jump-game-iv/
# Solved on 31st of August, 2025
from collections import defaultdict, deque


class Solution:
    def minJumps(self, arr: list[int]) -> int:
        """
        Calculates the minimum number of jumps to reach the last index of an array.

        Args:
            arr (list[int]): The input array of integers.
        Returns:
            int: The minimum number of jumps required, or -1 if the last index is unreachable.
        """
        n = len(arr)
        if n < 1 or n == 1:
            return 0

        # Map indices -> list of indices having that value
        val_indices = defaultdict(list)
        for i, v in enumerate(arr):
            val_indices[v].append(i)

        visited = [False] * n
        visited[0] = True
        q = deque([(0, 0)])

        while q:
            i, steps = q.popleft()
            # Reached end
            if i == (n -1):
                return steps

            # Neighbors: i - 1 and i + 1
            if i - 1 >= 0 and not visited[i - 1]:
                visited[i - 1] = True
                q.append((i - 1, steps + 1))
            if i + 1 < n and not visited[i + 1]:
                visited[i + 1] = True
                q.append((i + 1, steps + 1))

            # All indices j where arr[j] == arr[i]
            v = arr[i]
            # Iterate over saved indices
            for j in val_indices[v]:
                if not visited[j]:
                    visited[j] = True
                    q.append((j, steps + 1))
            val_indices[v].clear()

        # If unreachable
        return -1