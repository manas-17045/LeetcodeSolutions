// Leetcode 3568: Minimum Moves to Clean the Classroom
// https://leetcode.com/problems/minimum-moves-to-clean-the-classroom/
// Solved on 8th of November, 2025
import java.util.ArrayDeque;

class Solution {
    private static class State {
        int r;
        int c;
        int mask;
        int energy;
        int moves;
        State(int r, int c, int mask, int energy, int moves) {
            this.r = r;
            this.c = c;
            this.mask = mask;
            this.energy = energy;
            this.moves = moves;
        }
    }
    /**
     * Calculates the minimum number of moves required to clean all litter in the classroom.
     *
     * @param classroom A 2D array of characters representing the classroom grid. 'S' is the start, 'L' is litter, 'R' is a recharge station, 'X' is an obstacle.
     * @param energy The initial and maximum energy of the cleaner.
     * @return The minimum number of moves to clean all litter, or -1 if it's not possible.
     */
    public int minMoves(String[] classroom, int energy) {
        int rows = classroom.length;
        int cols = classroom[0].length();
        char[][] grid = new char[rows][cols];
        int startR = -1, startC = -1;
        int[][] litterIndex = new int[rows][cols];
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                litterIndex[i][j] = -1;
            }
        }
        int litterCount = 0;
        for (int i = 0; i < rows; i++) {
            String s = classroom[i];
            for (int j = 0; j < cols; j++) {
                char ch = s.charAt(j);
                grid[i][j] = ch;
                if (ch == 'S') {
                    startR = i;
                    startC = j;
                } else if (ch == 'L') {
                    litterIndex[i][j] = litterCount++;
                }
            }
        }
        if (litterCount == 0) {
            return 0;
        }
        int allMask = (1 << litterCount) - 1;
        int maxEnergy = energy;
        int[][][] bestEnergy = new int[rows][cols][1 << litterCount];
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                for (int k = 0; k < (1 << litterCount); k++) {
                    bestEnergy[i][j][k] = -1;
                }
            }
        }
        ArrayDeque<State> queue = new ArrayDeque<>();
        bestEnergy[startR][startC][0] = energy;
        queue.add(new State(startR, startC, 0, energy, 0));
        int[] dr = {-1,1,0,0};
        int[] dc = {0,0,-1,1};
        while (!queue.isEmpty()) {
            State cur = queue.poll();
            if (cur.mask == allMask) {
                return cur.moves;
            }
            if (cur.energy == 0) {
                continue;
            }
            for (int d = 0; d < 4; d++) {
                int nr = cur.r + dr[d];
                int nc = cur.c + dc[d];
                if (nr < 0 || nr >= rows || nc < 0 || nc >= cols) {
                    continue;
                }
                char cell = grid[nr][nc];
                if (cell == 'X') {
                    continue;
                }
                int nextEnergy = cur.energy - 1;
                if (cell == 'R') {
                    nextEnergy = maxEnergy;
                }
                int nextMask = cur.mask;
                if (cell == 'L') {
                    int idx = litterIndex[nr][nc];
                    if (idx >= 0) nextMask = cur.mask | (1 << idx);
                }
                if (bestEnergy[nr][nc][nextMask] < nextEnergy) {
                    bestEnergy[nr][nc][nextMask] = nextEnergy;
                    queue.add(new State(nr, nc, nextMask, nextEnergy, cur.moves + 1));
                }
            }
        }
        return -1;
    }
}