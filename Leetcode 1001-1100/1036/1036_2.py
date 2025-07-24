# Leetcode 1036: Escape a Large Maze
# https://leetcode.com/problems/escape-a-large-maze/
# Solved on 24th of July, 2025
from collections import deque


class Solution:
    def isEscapePossible(self, blocked: list[list[int]], source: list[int], target: list[int]) -> bool:
        """
        Determines if it's possible to escape from a source to a target in a grid, avoiding blocked cells.

        Args:
            blocked (list[list[int]]): A list of coordinates [x, y] representing blocked cells.
            source (list[int]): The starting coordinates [x, y].
            target (list[int]): The target coordinates [x, y].
        Returns:
            bool: True if escape is possible, False otherwise.
        """

        BLOCKED_SET = {tuple(pos) for pos in blocked}
        # Max cells to explore before confirming not blocked
        MAX_VISIT = 20000

        def bfs(start: list[int], goal: list[int]) -> bool:
            visited = set()
            queue = deque()
            queue.append(tuple(start))
            visited.add(tuple(start))

            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

            while queue and len(visited) < MAX_VISIT:
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < 10**6 and 0 <= ny < 10**6:
                        if (nx, ny) in BLOCKED_SET or (nx, ny) in visited:
                            continue
                        if [nx, ny] == goal:
                            return True
                        queue.append((nx, ny))
                        visited.add((nx, ny))

            return len(visited) >= MAX_VISIT

        return bfs(source, target) and bfs(target, source)