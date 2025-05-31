# Leetcode 909: Snakes and Ladders
# https://leetcode.com/problems/snakes-and-ladders/
# Solved on 31st of May, 2025
from collections import deque


class Solution:
    def snakesAndLadders(self, board: list[list[int]]) -> int:
        """
        Finds the minimum number of moves required to reach the target square (n*n)
        on a snakes and ladders board.

        Args:
            board: A list of lists representing the board. board[i][j] is the
                   destination square if there is a snake or ladder at that
                   position, otherwise it's -1.

        Returns:
            The minimum number of moves to reach the target square, or -1 if it's
            impossible.
        """
        # Get the dimension of the board
        n = len(board)
        # The label of the final square to reach.
        targetSquare = n * n

        # Helper function to convert a square's label to its (row, col) coordinates on the board.
        def getCoordinates(squareNum: int) -> tuple[int, int]:
            # Calculate 0-indexed row from the bottom of the board
            rFromBottom = (squareNum - 1) // n
            # Convert to 0-indexed row from the top (as used in a list of lists).
            boardRow = (n - 1) - rFromBottom

            # Calculate 0-indexed column within the conceptual Boustrophedon row.
            colInRow = (squareNum - 1) % n
            # For even rows from bottom (0, 2, ...), numbers go left-to-right.
            if rFromBottom % 2 == 0:
                # Column index is directly colInRow.
                boardCol = colInRow
            else:
                # For odd rows from bottom (1, 3, ...), numbers go right-to-left
                # Column index is mirrored
                boardCol = (n - 1) - colInRow

            # Return the (row, col) tuple
            return boardRow, boardCol

        # Initialize a queue for Breadth-First-Search(BFS). Stores (square_label, moves_taken).
        queue = deque([(1, 0)])
        # Initialize a set to keep track of visited squares to prevent cycles and redundant computations.
        visited = {1}

        # Start BFS. Continue as long as there are squares to explore in the queue.
        while queue:
            # Dequeue the current square's label and moves taken to reach it.
            currentSquare, moves = queue.popleft()

            # Simulate rolling a 6-sided die. Iterate through possible outcomes (1, 6).
            for diceRoll in range(1, 7):
                # Calculate the label of the square if we just moved by diceRoll.
                potentialNextSquareLabel = currentSquare + diceRoll

                # Determine the actual square label chosen based on die roll, capped at targetSquare.
                # This means if currentSquare + diceRoll > targetSquare, the effective chosen square is targetSquare.
                chosenSquareLabel = min(potentialNextSquareLabel, targetSquare)

                # Get the (ro, col) coordinates of this chosen square on the board.
                r, c = getCoordinates(chosenSquareLabel)

                # Check if the square at (r, c) has a snake or a ladder.
                if board[r][c] != -1:
                    # If yes, the player is moved to the destination of the snake/ladder.
                    finalDestinationSquare = board[r][c]
                else:
                    # If no, the player stays on the chosenSquareLabel.
                    finalDestinationSquare = chosenSquareLabel

                # Check if this final destination is the target square.
                if finalDestinationSquare == targetSquare:
                    # If so, return total moves (current moves + this roll).
                    return moves + 1

                # If the final destination square has not yet been visisted yet in a path
                if finalDestinationSquare not in visited:
                    # Mark it as visited
                    visited.add(finalDestinationSquare)
                    # Enqueue this state (finalDestinationSquare, moves + 1) for further exploration.
                    queue.append((finalDestinationSquare, moves + 1))

        # If the queue becomes empty and the target square was not reached, it's impossible.
        return -1