// Leetcode 1861: Rotating the Box
// https://leetcode.com/problems/rotating-the-box/
// Solved on 13th of November, 2025
class Solution {
    /**
     * Rotates a given box grid 90 degrees clockwise and simulates the effect of gravity.
     * Stones ('#') fall down until they hit an obstacle ('*') or another stone.
     *
     * @param boxGrid The input 2D character array representing the box.
     * @return A new 2D character array representing the rotated and settled box.
     */
    public char[][] rotateTheBox(char[][] boxGrid) {
        int m = boxGrid.length;
        int n = boxGrid[0].length;
        for (int i = 0; i < m; i++) {
            int empty = n - 1;
            for (int j = n - 1; j >= 0; j--) {
                char c = boxGrid[i][j];
                if (c == '*') {
                    empty = j - 1;
                } else if (c == '#') {
                    if (empty != j) {
                        boxGrid[i][empty] = '#';
                        boxGrid[i][j] = '.';
                    }
                    empty--;
                }
            }
        }
        char[][] result = new char[n][m];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                result[i][j] = '.';
            }
        }
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                result[j][m - 1 - i] = boxGrid[i][j];
            }
        }
        return result;
    }
}