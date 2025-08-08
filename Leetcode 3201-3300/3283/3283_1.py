# Leetcode 3283: Maximum Number of Moves to Kill All Pawns
# https://leetcode.com/problems/maximum-number-of-moves-to-kill-all-pawns/
# Solved on 8th of August, 2025
from collections import deque
from functools import lru_cache


class Solution:
    def maxMoves(self, kx: int, ky: int, positions: list[list[int]]) -> int:
        """
        Calculates the maximum number of moves required to kill all pawns.

        Args:
            kx (int): The initial x-coordinate of the knight.
            ky (int): The initial y-coordinate of the knight.
            positions (list[list[int]]): A list of [x, y] coordinates for each pawn.

        Returns:
            int: The maximum number of moves to kill all pawns.
        """

        DIRS = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]

        def get_min_moves(start_x: int, start_y: int, target_x: int, target_y: int) -> int:
            if start_x == target_x and start_y == target_y:
                return 0

            queue = deque([(start_x, start_y, 0)])
            visited = set([(start_x, start_y)])

            while queue:
                x, y, moves = queue.popleft()

                for dx, dy in DIRS:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < 50 and 0 <= ny < 50 and (nx, ny) not in visited:
                        if nx == target_x and ny == target_y:
                            return moves + 1
                        visited.add((nx, ny))
                        queue.append((nx, ny, moves + 1))

            return int('inf')  # Should never reach here for valid positions

        n = len(positions)

        # Precompute distances between knight and all pawns, and between all pairs of pawns
        dist_from_knight = {}
        dist_between_pawns = {}

        # Distance from knight to each pawn
        for i, (px, py) in enumerate(positions):
            dist_from_knight[i] = get_min_moves(kx, ky, px, py)

        # Distance between each pair of pawns
        for i in range(n):
            for j in range(n):
                if i != j:
                    px1, py1 = positions[i]
                    px2, py2 = positions[j]
                    dist_between_pawns[(i, j)] = get_min_moves(px1, py1, px2, py2)

        # Memoized DP function
        @lru_cache(maxsize=None)
        def dp(mask: int, last_pos: int, is_alice_turn: bool) -> int:
            if mask == (1 << n) - 1:  # All pawns captured
                return 0

            if is_alice_turn:
                result = -float('inf')
                for i in range(n):
                    if mask & (1 << i) == 0:  # Pawn i not captured yet
                        if last_pos == -1:  # Starting from knight's position
                            moves = dist_from_knight[i]
                        else:  # Moving from last pawn position
                            moves = dist_between_pawns[(last_pos, i)]

                        result = max(result, moves + dp(mask | (1 << i), i, False))
                return result
            else:  # Bob's turn (minimizing)
                result = float('inf')
                for i in range(n):
                    if mask & (1 << i) == 0:  # Pawn i not captured yet
                        if last_pos == -1:  # Starting from knight's position
                            moves = dist_from_knight[i]
                        else:  # Moving from last pawn position
                            moves = dist_between_pawns[(last_pos, i)]

                        result = min(result, moves + dp(mask | (1 << i), i, True))
                return result

        return dp(0, -1, True)