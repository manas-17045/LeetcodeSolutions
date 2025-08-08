# Leetcode 3283: Maximum Number of Moves to Kill All Pawns
# https://leetcode.com/problems/maximum-number-of-moves-to-kill-all-pawns/
# Solved on 8th of August, 2025
from collections import deque
from functools import lru_cache


class Solution:
    def maxMoves(self, kx: int, ky: int, positions: list[list[int]]) -> int:
        """
        Calculates the maximum number of moves a knight can make to capture all pawns,
        considering an alternating turn-based game between Alice (maximizing moves)
        and Bob (minimizing moves).
        :param kx: Initial x-coordinate of the knight.
        :param ky: Initial y-coordinate of the knight.
        :param positions: A list of [x, y] coordinates for each pawn.
        :return: The total number of moves if all pawns can be captured, otherwise -1.
        """
        # Problem states a 50 x 50 board (coordinates range[0...49])
        N = 50

        # Keep pawn nodes and the start node as our relevant positions
        pawns = [(x, y) for x, y in positions]
        start = (kx, ky)
        nodes = pawns + [start]  # indices 0..m-1 are pawns, m is start
        m = len(pawns)

        # Knight moves
        KNIGHT_DELTAS = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

        # BFS from a source on the fixed 50x50 board, returns dist grid
        def bfs_from(sx: int, sy: int):
            dist = [[-1] * N for _ in range(N)]
            if not (0 <= sx < N and 0 <= sy < N):
                return dist
            dq = deque()
            dq.append((sx, sy))
            dist[sx][sy] = 0
            while dq:
                x, y = dq.popleft()
                d = dist[x][y]
                for dx, dy in KNIGHT_DELTAS:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < N and 0 <= ny < N and dist[nx][ny] == -1:
                        dist[nx][ny] = d + 1
                        dq.append((nx, ny))
            return dist

        # Precompute BFS-distances from each relevant node (each pawn + start)
        precomputed = [bfs_from(x, y) for (x, y) in nodes]

        # Build pairwise distance matrix between relevant nodes
        INF = 10 ** 9
        dist_matrix = [[INF] * (m + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            for j in range(m + 1):
                if i == j:
                    dist_matrix[i][j] = 0
                else:
                    tx, ty = nodes[j]
                    d = precomputed[i][tx][ty]
                    if d != -1:
                        dist_matrix[i][j] = d

        FULL = (1 << m) - 1

        # DP minimax: state (mask, last_index)
        # returns (possible, best_total_remaining_moves)
        @lru_cache(None)
        def dfs(mask: int, last: int):
            if mask == FULL:
                return True, 0  # no more pawns: 0 further moves

            bits = mask.bit_count()
            alice_turn = (bits % 2 == 0)  # Alice moves when captured-count is even

            best_val = None
            for i in range(m):
                if (mask >> i) & 1:
                    continue
                d = dist_matrix[last][i]
                if d >= INF:
                    # unreachable pawn from current position, skip
                    continue
                possible_next, val_next = dfs(mask | (1 << i), i)
                if not possible_next:
                    continue
                total = d + val_next
                if best_val is None:
                    best_val = total
                else:
                    if alice_turn:
                        if total > best_val:
                            best_val = total
                    else:
                        if total < best_val:
                            best_val = total

            if best_val is None:
                # no feasible way to capture remaining pawns
                return False, 0
            return True, best_val

        # Start state: no pawns captured, knight at index m (start)
        possible, ans = dfs(0, m)
        return ans if possible else -1