# Leetcode 2056: Number of Valid Move Combinations On Chessboard
# https://leetcode.com/problems/number-of-valid-move-combinations-on-chessboard/
# Solved on 6th of December, 2025
class Solution:
    def countCombinations(self, pieces: list[str], positions: list[list[str]]) -> int:
        """
        Counts the number of valid move combinations on a chessboard.

        Args:
            pieces: A list of strings representing the types of chess pieces.
            positions: A list of lists of integers representing the initial positions of the pieces.
        Returns:
            The total number of valid move combinations.
        """
        n = len(pieces)
        positions = [[r - 1, c - 1] for r, c in positions]

        rookDirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        bishopDirs = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        queenDirs = rookDirs + bishopDirs

        pieceDirs = {
            "rook": rookDirs,
            "bishop": bishopDirs,
            "queen": queenDirs
        }

        allMoves = []
        for i in range(n):
            movesForPiece = []
            r, c = positions[i]
            movesForPiece.append((0, 0, 0, r, c))

            for dr, dc in pieceDirs[pieces[i]]:
                step = 1
                while True:
                    nr, nc = r + dr * step, c + dc * step
                    if 0 <= nr < 8 and 0 <= nc < 8:
                        movesForPiece.append((dr, dc, step, r, c))
                        step += 1
                    else:
                        break
            allMoves.append(movesForPiece)

        def hasCollision(move1, move2):
            dr1, dc1, s1, r1, c1 = move1
            dr2, dc2, s2, r2, c2 = move2

            for t in range(1, 9):
                if t > s1 and t > s2:
                    break

                cr1 = r1 + dr1 * min(t, s1)
                cc1 = c1 + dc1 * min(t, s1)

                cr2 = r2 + dr2 * min(t, s2)
                cc2 = c2 + dc2 * min(t, s2)

                if cr1 == cr2 and cc1 == cc2:
                    return True
            return False

        self.validCombinations = 0

        def backtrack(idx, activeMoves):
            if idx == n:
                self.validCombinations += 1
                return

            for move in allMoves[idx]:
                isValid = True
                for prevMove in activeMoves:
                    if hasCollision(move, prevMove):
                        isValid = False
                        break

                if isValid:
                    activeMoves.append(move)
                    backtrack(idx + 1, activeMoves)
                    activeMoves.pop()

        backtrack(0, [])
        return self.validCombinations