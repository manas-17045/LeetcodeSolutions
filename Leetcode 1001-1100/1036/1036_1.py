# Leetcode 1036: Escape a Large Maze
# https://leetcode.com/problems/escape-a-large-maze/
# Solved on 24th of July, 2025
import collections


class Solution:
    def isEscapePossible(self, blocked: list[list[int]], source: list[int], target: list[int]) -> bool:
        """
        Determines if it's possible to escape a large maze from source to target, avoiding blocked cells.
        Args:
            blocked (list[list[int]]): A list of coordinates [r, c] representing blocked cells.
            source (list[int]): The starting coordinates [r, c].
            target (list[int]): The target coordinates [r, c].
        Returns:
            bool: True if escape is possible, False otherwise.
        """

        if not blocked:
            return True

        blockedSet = set(map(tuple, blocked))
        gridLimit = 1_000_000

        def runBfs(start, end):
            bfsQueue = collections.deque([tuple(start)])
            visited = {tuple[start]}

            maxArea = len(blocked) * (len(blocked) - 1) // 2

            while bfsQueue:
                if len(visited) > maxArea:
                    return True

                x, y = bfsQueue.popleft()

                if [x, y] == end:
                    return True

                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nx = x + dx
                    ny = y + dy
                    nextPos = (nx, ny)

                    if not (0 <= nx < gridLimit and 0 <= ny < gridLimit):
                        continue

                    if nextPos in visited or nextPos in blockedSet:
                        continue

                    visited.add(nextPos)
                    bfsQueue.append(nextPos)

            return False

        return runBfs(source, target) and runBfs(target, source)