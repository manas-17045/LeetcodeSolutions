// Leetcode 835: Image Overlap
// https://leetcode.com/problems/image-overlap/
// Solved on 13th of September, 2026
class Solution {
    /**
     * Calculates the maximum possible overlap of 1s between two binary images
     * by translating one image in any direction (up, down, left, right).
     *
     * @param img1 the first binary square matrix
     * @param img2 the second binary square matrix
     * @return the maximum number of overlapping 1s after optimal translation
     */
    public int largestOverlap(int[][] img1, int[][] img2) {
        int n = img1.length;
        int[] bits1 = new int[n];
        int[] bits2 = new int[n];

        for (int row = 0; row < n; row++) {
            for (int col = 0; col < n; col++) {
                bits1[row] = (bits1[row] << 1) | img1[row][col];
                bits2[row] = (bits2[row] << 1) | img2[row][col];
            }
        }

        int mask = (1 << n) - 1;
        int maxOverlap = 0;

        for (int rowShift = -n + 1; rowShift < n; rowShift++) {
            int rowStart = Math.max(0, -rowShift);
            int rowEnd = Math.min(n, n - rowShift);

            for (int colShift = -n + 1; colShift < n; colShift++) {
                int currentOverlap = 0;

                for (int row = rowStart; row < rowEnd; row++) {
                    int shiftedRow = (colShift >= 0)
                            ? (bits1[row] >>> colShift)
                            : ((bits1[row] << -colShift) & mask);
                    currentOverlap += Integer.bitCount(shiftedRow & bits2[row + rowShift]);
                }

                if (currentOverlap > maxOverlap) {
                    maxOverlap = currentOverlap;
                }
            }
        }

        return maxOverlap;
    }
}