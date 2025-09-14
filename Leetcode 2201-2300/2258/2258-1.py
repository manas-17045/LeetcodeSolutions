# Leetcode 2258: Escape the Spreading Fire
# https://leetcode.com/problems/escape-the-spreading-fire/
# Solved on 14th of September, 2025
import collections


class Solution:
    def maximumMinutes(self, grid: list[list[int]]) -> int:
        """
        Calculates the maximum number of minutes a person can wait at the starting cell (0, 0)
        before moving to the safehouse (rows-1, cols-1) without being caught by spreading fire.

        Args:
            grid: A 2D list of integers representing the grid.
                  0: Grass (can be traversed)
                  1: Fire (starting point of fire)
                  2: Wall (cannot be traversed)
        Returns:
            The maximum number of minutes the person can wait. If it's possible to reach the safehouse
            even if the fire never reaches the safehouse, return 10^9. If it's impossible to reach
            the safehouse, return -1.
        """
        rows = len(grid)
        cols = len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        fireTime = [[float('inf')] * cols for _ in range(rows)]
        q = collections.deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    q.append((r, c, 0))
                    fireTime[r][c] = 0
                elif grid[r][c] == 2:
                    fireTime[r][c] = -1

        while q:
            r, c, currentTime = q.popleft()
            for dr, dc in directions:
                nextRow, nextCol = r + dr, c + dc
                if 0 <= nextRow < rows and 0 <= nextCol < cols and grid[nextRow][nextCol] == 0 and fireTime[nextRow][
                    nextCol] == float('inf'):
                    fireTime[nextRow][nextCol] = currentTime + 1
                    q.append((nextRow, nextCol, currentTime + 1))

        def canReach(waitTime):
            if waitTime >= fireTime[0][0]:
                return False

            qPerson = collections.deque([(0, 0, waitTime)])
            visited = {(0, 0)}

            while qPerson:
                r, c, personTime = qPerson.popleft()

                if r == rows - 1 and c == cols - 1:
                    return True

                for dr, dc in directions:
                    nextRow, nextCol = r + dr, c + dc

                    if not (0 <= nextRow < rows and 0 <= nextCol < cols and grid[nextRow][nextCol] == 0 and (nextRow,
                                                                                                             nextCol) not in visited):
                        continue

                    arrivalTime = personTime + 1

                    if arrivalTime <= fireTime[nextRow][nextCol]:
                        if nextRow == rows - 1 and nextCol == cols - 1:
                            return True

                        if arrivalTime < fireTime[nextRow][nextCol]:
                            visited.add((nextRow, nextCol))
                            qPerson.append((nextRow, nextCol, arrivalTime))
            return False

        low = 0
        high = rows * cols
        ans = -1

        while low <= high:
            mid = low + (high - low) // 2
            if canReach(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans if ans != rows * cols else 10**9