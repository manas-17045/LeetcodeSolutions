# Leetcode 909: Snakes and Ladders
# https://leetcode.com/problems/snakes-and-ladders/
# Solved on 31st of May, 2025
from collections import deque


class Solution:
    def snakesAndLadders(self, board: list[list[int]]) -> int:
        """
        Finds the minimum number of moves required to reach the last square
        of a Snakes and Ladders board.

        Args:
            board: A 2D list representing the board. -1 indicates no snake or
                   ladder, otherwise it's the destination square.

        Returns:
            The minimum number of moves to reach the last square, or -1 if
            it's impossible.
        """

        n = len(board)

        def idToRc(s: int) -> (int, int):
            # Which 0-based row from bottom this square is on
            rowFromBottom = (s - 1) // n
            # Actual row index in the 2D array (0-indexed from top)
            r = n - 1 - rowFromBottom
            # Position within that row (0-based)
            offset = (s - 1) % n
            # If rowFromBottom is even, that row goes left0-to-right; if odd, right-to-left
            if rowFromBottom % 2 == 0:
                c = offset
            else:
                c = n - 1 - offset
            return r, c

        target = n * n
        visited = [False] * (target + 1)
        queue = deque()
        # Start from square 1, with 0 moves taken so far
        queue.append((1, 0))
        visited[1] = True

        while queue:
            curr, moves = queue.popleft()
            if curr == target:
                return moves

            # Try all possible die rolls 1 through 6
            for step in range(1, 7):
                nxt = curr + step
                if nxt > target:
                    break

                r, c = idToRc(nxt)
                # If there's a snake or ladder, jump to its destination
                if board[r][c] != -1:
                    dest = board[r][c]
                else:
                    dest = nxt

                if not visited[dest]:
                    visited[dest] = True
                    queue.append((dest, moves + 1))

        # If we exhaust the queue without reaching the last square, it's impossible
        return -1