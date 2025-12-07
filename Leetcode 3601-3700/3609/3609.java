// Leetcode 3609: Minimum Moves to Reach Target in Grid
// https://leetcode.com/problems/minimum-moves-to-reach-target-in-grid/
// Solved on 7th of December, 2025
class Solution {
    /**
     * Calculates the minimum number of moves to reach a target coordinate (tx, ty) from a starting coordinate (sx, sy).
     * The allowed moves are: (x, y) -> (x + y, y), (x, y) -> (x, x + y), or (x, y) -> (x/2, y) if x is even, or (x, y) -> (x, y/2) if y is even.
     *
     * @param sx The starting x-coordinate.
     * @param sy The starting y-coordinate.
     * @param tx The target x-coordinate.
     * @param ty The target y-coordinate.
     * @return The minimum number of moves, or -1 if the target is unreachable.
     */
    public int minMoves(int sx, int sy, int tx, int ty) {
        int moves = 0;
        while (tx >= sx && ty >= sy) {
            if (tx == sx && ty == sy) {
                return moves;
            }

            if (tx == ty) {
                if (sx == 0) {
                    if (sy == 0) {
                        return -1;
                        }
                    if (tx % sy == 0) {
                        int ratio = tx / sy;
                        if ((ratio & (ratio - 1)) == 0) {
                            return moves + 1 + (31 - Integer.numberOfLeadingZeros(ratio));
                        }
                    }
                    return -1;
                } else if (sy == 0) {
                    if (sx == 0) {
                        return -1;
                    }
                    if (ty % sx == 0) {
                        int ratio = ty / sx;
                        if ((ratio & (ratio - 1)) == 0) {
                            return moves + 1 + (31 - Integer.numberOfLeadingZeros(ratio));
                        }
                    }
                    return -1;
                }
                return -1;
            }

            if (tx > ty) {
                if (tx > 2 * ty) {
                    if (tx % 2 != 0) {
                        return -1;
                    }
                    tx /= 2;
                    moves++;
                } else {
                    tx -= ty;
                    moves++;
                }
            } else {
                if (ty > 2 * tx) {
                    if (ty % 2 != 0) {
                        return -1;
                    }
                    ty /= 2;
                    moves++;
                } else {
                    ty -= tx;
                    moves++;
                }
            }
        }
        return -1;
    }
}