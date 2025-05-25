# Leetcode 1728: Cat and Mouse II
# https://leetcode.com/problems/cat-and-mouse-ii/
# Solved on 19th of May, 2025
from functools import lru_cache


class Solution:
    def canMouseWin(self, grid: list[str], catJump: int, mouseJump: int) -> bool:
        """
        Determines if the mouse can win the game against the cat.

        The game is played on a grid where the mouse and cat try to reach food before the other.
        The mouse moves first, followed by the cat.  Each can move up to a certain jump distance
        in any of the four cardinal directions.  Walls ('#') block movement.

        Args:
            grid: A list of strings representing the game board. 'M' is the mouse's starting position,
                  'C' is the cat's starting position, 'F' is the food, and '#' are walls.
            catJump: The maximum jump distance for the cat.
            mouseJump: The maximum jump distance for the mouse.
        Returns:
            True if the mouse can win, False otherwise.
        """

        rows, cols = len(grid), len(grid[0])
        # Locate start positions and food
        mouse_start = cat_start = food = None
        for r in range(rows):
            for c in range(cols):
                ch = grid[r][c]
                if ch == 'M':
                    mouse_start = (r, c)
                elif ch == 'C':
                    cat_start = (r, c)
                elif ch == 'F':
                    food = (r, c)

        # Precompute reachable positions for a given jump limit
        def build_moves(jump: int) -> dict:
            moves = {}
            for r in range(rows):
                for c in range(cols):
                    if grid[r][c] == '#':
                        continue
                    src = (r, c)
                    nbrs = [src]    # Staying in place is allowed
                    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        for step in range(1, jump + 1):
                            nr, nc = r + dr * step, c + dc * step
                            if not ((0 <= nr < rows) and (0 <= nc < cols)):
                                break
                            if grid[nr][nc] == '#':
                                break
                            nbrs.append((nr, nc))
                    moves[src] = nbrs
            return moves

        mouse_moves = build_moves(mouseJump)
        cat_moves = build_moves(catJump)

        # Depth cut-off: If mouse has not won within 2 * R * C turns, cat wins
        MAX_TURNS = 2 * rows * cols

        @lru_cache(None)
        def dfs(mouse: tuple[int, int], cat: tuple[int, int], turn: int, depth: int) -> bool:
            # turn: 0 = mouse to move; 1 = cat to move
            # depth counts total moves so far
            if depth >= MAX_TURNS:
                return False    # cat wins on timeout
            if mouse == cat:
                return False    # caught
            if cat == food:
                return False    # Cat got food first
            if mouse == food:
                return True     # mouse got food

            if turn == 0:
                # Mouse's move: if any move leads to a win, it wins
                for nxt in mouse_moves[mouse]:
                    if dfs(nxt, cat, 1, depth + 1):
                        return True
                return False
            else:
                # Cat's move: if any move leads to mouse losing, cat will choose that
                for nxt in cat_moves[cat]:
                    if not dfs(mouse, nxt, 0, depth + 1):
                        return False
                return True

        return dfs(mouse_start, cat_start, 0, 0)