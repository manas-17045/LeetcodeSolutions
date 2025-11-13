// Leetcode 1349: Maximum Students Taking Exam
// https://leetcode.com/problems/maximum-students-taking-exam/
// Solved on 13th of November, 2025
import java.util.ArrayList;
import java.util.List;

class Solution {
    /**
     * Calculates the maximum number of students that can be seated in a classroom
     * such that no two students are adjacent (horizontally, vertically, or diagonally).
     *
     * @param seats A 2D array of characters representing the classroom layout.
     *              '.' denotes an empty seat, '#' denotes a broken seat.
     * @return The maximum number of students that can be seated.
     */
    public int maxStudents(char[][] seats) {
        if (seats == null || seats.length == 0) {
            return 0;
        }
        int m = seats.length;
        int n = seats[0].length;
        int maxMask = 1 << n;

        int[] bitCount = new int[maxMask];
        for (int mask = 0; mask < maxMask; mask++) {
            bitCount[mask] = Integer.bitCount(mask);
        }

        int[] availMask = new int[m];
        for (int i = 0; i < m; i++) {
            int mask = 0;
            for (int j = 0; j < n; j++) {
                if (seats[i][j] == '.') {
                    mask |= (1 << j);
                }
            }
            availMask[i] = mask;
        }

        List<Integer>[] validPerRow = new ArrayList[m];
        for (int i = 0; i < m; i++) {
            validPerRow[i] = new ArrayList<>();
            int allow = availMask[i];
            for (int mask = 0; mask < maxMask; mask++) {
                if ((mask & ~allow) != 0) {
                    continue;
                }
                if ((mask & (mask << 1)) != 0) {
                    continue;
                }
                validPerRow[i].add(mask);
            }
        }

        int[] prevDp = new int[maxMask];
        for (int i = 0; i < maxMask; i++) {
            prevDp[i] = -1;
        }
        prevDp[0] = 0;

        for (int row = 0; row < m; row++) {
            int[] currDp = new int[maxMask];
            for (int i = 0; i < maxMask; i++) {
                currDp[i] = -1;
            }

            for (int mask : validPerRow[row]) {
                for (int p = 0; p < maxMask; p++) {
                    if (prevDp[p] < 0) {
                        continue;
                    }
                    if ((mask & (p << 1)) != 0) {
                        continue;
                    }
                    if ((mask & (p >> 1)) != 0) {
                        continue;
                    }

                    int val = prevDp[p] + bitCount[mask];
                    if (val > currDp[mask]) {
                        currDp[mask] = val;
                    }
                }
            }
            prevDp = currDp;
        }

        int ans = 0;
        for (int v : prevDp) {
            if (v > ans) {
                ans = v;
            }
        }
        return ans;
    }
}