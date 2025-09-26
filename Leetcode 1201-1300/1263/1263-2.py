# Leetcode 1263: Minimum Moves to Move a Box to Their Target Location
# https://leetcode.com/problems/minimum-moves-to-move-a-box-to-their-target-location/
# Solved on 25th of September, 2025
import heapq
from collections import deque


class Solution:
    def minPushBox(self, grid: list[list[str]]) -> int:
        """
        Calculates the minimum number of pushes required to move a box from its starting position to a target position.

        Args:
            grid (list[list[str]]): A 2D grid representing the game board.

        Returns:
            int: The minimum number of pushes required, or -1 if the target is unreachable.
        """
        m = len(grid)
        if m == 0:
            return -1
        n = len(grid[0])

        # Convert row strings to lists if needed
        for i in range(m):
            if isinstance(grid[i], str):
                grid[i] = list(grid[i])

        sx = sy = bx = by = tx = ty = -1
        for i in range(m):
            for j in range(n):
                c = grid[i][j]
                if c == 'S':
                    sx, sy = i, j
                elif c == 'B':
                    bx, by = i, j
                elif c == 'T':
                    tx, ty = i, j

        # helper to check if a coordinate is inside and not a wall
        def ok(x: int, y: int) -> bool:
            return 0 <= x < m and 0 <= y < n and grid[x][y] != '#'

        # BFS to check if player can reach (tx,ty) from (px,py) without crossing the box at (bx_block, by_block)
        def player_reachable(px: int, py: int, target_x: int, target_y: int, bx_block: int, by_block: int) -> bool:
            if not ok(target_x, target_y):
                return False
            if (px, py) == (target_x, target_y):
                return True
            q = deque()
            q.append((px, py))
            seen = [[False] * n for _ in range(m)]
            seen[px][py] = True
            seen[bx_block][by_block] = True  # treat box as obstacle for the player's movement
            while q:
                x, y = q.popleft()
                for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and not seen[nx][ny] and grid[nx][ny] != '#':
                        if (nx, ny) == (target_x, target_y):
                            return True
                        seen[nx][ny] = True
                        q.append((nx, ny))
            return False

        # Dijkstra-like: minimize pushes
        # State: (pushes, box_x, box_y, player_x, player_y)
        start = (0, bx, by, sx, sy)
        heap = [start]
        # store best pushes for a given (box_x,box_y,player_x,player_y)
        # using dictionary to prune
        dist = {}
        dist[(bx, by, sx, sy)] = 0

        while heap:
            pushes, cbx, cby, px, py = heapq.heappop(heap)
            # if this state has higher cost than best known, skip
            if dist.get((cbx, cby, px, py), float('inf')) < pushes:
                continue
            # if box at target
            if (cbx, cby) == (tx, ty):
                return pushes

            # try to push box in each direction
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nbx, nby = cbx + dx, cby + dy  # new box position after push
                player_needed_x, player_needed_y = cbx - dx, cby - dy  # location player must reach to push

                # both target cell for box and required player cell must be valid (inside, not wall)
                if not (0 <= nbx < m and 0 <= nby < n and ok(nbx, nby)):
                    continue
                if not (0 <= player_needed_x < m and 0 <= player_needed_y < n and ok(player_needed_x, player_needed_y)):
                    continue

                # check if player can reach player_needed cell without crossing the current box cell
                if not player_reachable(px, py, player_needed_x, player_needed_y, cbx, cby):
                    continue

                new_pushes = pushes + 1
                # after pushing, player occupies the box's old cell
                new_px, new_py = cbx, cby
                key = (nbx, nby, new_px, new_py)
                if dist.get(key, float('inf')) > new_pushes:
                    dist[key] = new_pushes
                    heapq.heappush(heap, (new_pushes, nbx, nby, new_px, new_py))

        return -1