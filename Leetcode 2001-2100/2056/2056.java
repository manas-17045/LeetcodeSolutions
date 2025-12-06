// Leetcode 2056: Number of Valid Move Combinations On Chessboard
// https://leetcode.com/problems/number-of-valid-move-combinations-on-chessboard/
// Solved on 6th of December, 2025
import java.util.ArrayList;
import java.util.List;

class Solution {
    private final int[][] directions = {
        {1, 0}, {-1, 0}, {0, 1}, {0, -1}, 
        {1, 1}, {1, -1}, {-1, 1}, {-1, -1}
    };

    /**
     * Counts the number of valid move combinations for a given set of chess pieces.
     * @param pieces An array of strings representing the type of each piece (e.g., "rook", "bishop", "queen").
     * @param positions An array of integer arrays, where each inner array represents the initial [row, column] of a piece.
     * @return The total number of valid move combinations.
     */
    public int countCombinations(String[] pieces, int[][] positions) {
        List<List<int[]>> allPieceMoves = new ArrayList<>();
        for (int i = 0; i < pieces.length; i++) {
            List<int[]> moves = new ArrayList<>();
            int r = positions[i][0];
            int c = positions[i][1];
            moves.add(new int[]{r, c, 0, 0, 0});
            
            int startDir = 0, endDir = 8;
            if (pieces[i].equals("rook")) {
                endDir = 4;
            } else if (pieces[i].equals("bishop")) {
                startDir = 4;
            }
            
            for (int d = startDir; d < endDir; d++) {
                int dr = directions[d][0];
                int dc = directions[d][1];
                for (int step = 1; step < 8; step++) {
                    int nr = r + dr * step;
                    int nc = c + dc * step;
                    if (nr < 1 || nr > 8 || nc < 1 || nc > 8) {
                        break;
                    }
                    moves.add(new int[]{r, c, dr, dc, step});
                }
            }
            allPieceMoves.add(moves);
        }
        return countValidCombinations(0, new ArrayList<>(), allPieceMoves);
    }

    private int countValidCombinations(int index, List<int[]> activeMoves, List<List<int[]>> allPieceMoves) {
        if (index == allPieceMoves.size()) {
            return 1;
        }

        int count = 0;
        for (int[] move : allPieceMoves.get(index)) {
            if (isValidMove(activeMoves, move)) {
                activeMoves.add(move);
                count += countValidCombinations(index + 1, activeMoves, allPieceMoves);
                activeMoves.remove(activeMoves.size() - 1);
            }
        }
        return count;
    }

    private boolean isValidMove(java.util.List<int[]> activeMoves, int[] newMove) {
        for (int[] active : activeMoves) {
            if (detectCollision(active, newMove)) {
                return false;
            }
        }
        return true;
    }

    private boolean detectCollision(int[] move1, int[] move2) {
        int r1 = move1[0], c1 = move1[1], dr1 = move1[2], dc1 = move1[3], s1 = move1[4];
        int r2 = move2[0], c2 = move2[1], dr2 = move2[2], dc2 = move2[3], s2 = move2[4];
        
        for (int t = 1; t <= 8; t++) {
            int curR1 = r1 + dr1 * (t < s1 ? t : s1);
            int curC1 = c1 + dc1 * (t < s1 ? t : s1);
            int curR2 = r2 + dr2 * (t < s2 ? t : s2);
            int curC2 = c2 + dc2 * (t < s2 ? t : s2);
            
            if (curR1 == curR2 && curC1 == curC2) {
                return true;
            }
        }
        return false;
    }
}