# Leetcode 2258: Escape the Spreading Fire
# https://leetcode.com/problems/escape-the-spreading-fire/
# Solved on 14th of September, 2025
from collections import deque


class Solution:
    def maximumMinutes(self, grid: list[list[int]]) -> int:
        """
        Calculates the maximum minutes one can wait before entering a burning grid to reach a safehouse.

        Args:
            grid: A 2D list representing the grid. 0 for empty, 1 for fire, 2 for wall.
        Returns:
            The maximum minutes one can wait. Returns -1 if the safehouse is unreachable,
            or 10^9 if an arbitrarily long wait is possible.
        """
        m, n = len(grid), len(grid[0])
        INF = 10**18

        # Multi-source BFS to compute fire arrival times
        fire_time = [[INF] * n for _ in range(m)]
        q = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fire_time[i][j] = 0
                    q.append((i, j))

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while q:
            x, y = q.popleft()
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] != 2:
                    nt = fire_time[x][y] + 1
                    if fire_time[nx][ny] > nt:
                        fire_time[nx][ny] = nt
                        q.append((nx, ny))

        # BFS to check if safehouse is reachable with a given wait time
        def can_escape(wait: int) -> bool:
            if wait >= fire_time[0][0]:
                return False

            visited = [[False] * n for _ in range(m)]
            dq = deque([(0, 0, wait)])
            visited[0][0] = True

            while dq:
                x, y, t = dq.popleft()
                if (x, y) == (m - 1, n - 1):
                    return t <= fire_time[x][y]

                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] != 2:
                        arrive_time = t + 1
                        if arrive_time < fire_time[nx][ny] or ((nx, ny) == (m - 1, n - 1) and arrive_time == fire_time[nx][ny]):
                            visited[nx][ny] = True
                            dq.append((nx, ny, arrive_time))

            return False

        LIMIT = 10**9
        if can_escape(LIMIT):
            return LIMIT

        # Binary search for maximum wait time
        lo, hi = 0, LIMIT - 1
        ans = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if can_escape(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1

        return ans