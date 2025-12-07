# Leetcode 3609: Minimum Moves to Reach Target in Grid
# https://leetcode.com/problems/minimum-moves-to-reach-target-in-grid/
# Solved on 7th of December, 2025
class Solution:
    def minMoves(self, sx: int, sy: int, tx: int, ty: int) -> int:
        """
        Calculates the minimum number of moves to reach a target coordinate (tx, ty) from a starting coordinate (sx, sy).

        Args:
            sx (int): The starting x-coordinate.
            sy (int): The starting y-coordinate.
            tx (int): The target x-coordinate.
            ty (int): The target y-coordinate.

        Returns:
            int: The minimum number of moves, or -1 if the target is unreachable.
        """
        moves = 0
        while tx >= sx and ty >= sy:
            if tx == sx and ty == sy:
                return moves

            if tx == ty:
                if sx == 0:
                    if sy == 0:
                        return -1
                    if tx % sy == 0 and ((tx // sy) & ((tx // sy) - 1)) == 0:
                        return moves + 1 + (tx // sy).bit_length() - 1
                if sy == 0:
                    if sx == 0:
                        return -1
                    if ty % sx == 0 and ((ty // sx) & ((ty // sx) - 1)) == 0:
                        return moves + 1 + (ty // sx).bit_length() - 1
                return -1

            if tx > ty:
                if tx > 2 * ty:
                    if tx % 2 != 0:
                        return -1
                    tx //= 2
                    moves += 1
                else:
                    tx -= ty
                    moves += 1
            else:
                if ty > 2 * tx:
                    if ty % 2 != 0:
                        return -1
                    ty //= 2
                    moves += 1
                else:
                    ty -= tx
                    moves += 1
        return -1