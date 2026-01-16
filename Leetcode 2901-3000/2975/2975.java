// Leetcode 2975: Maximum Square Area by Removing Fences From a Field
// https://leetcode.com/problems/maximum-square-area-by-removing-fences-from-a-field/
// Solved on 16th of January, 2026
import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

class Solution {
    /**
     * Calculates the maximum possible square area that can be formed by removing fences.
     *
     * @param m The height of the field.
     * @param n The width of the field.
     * @param hFences An array of integers representing the positions of horizontal fences.
     * @param vFences An array of integers representing the positions of vertical fences.
     * @return The maximum square area, or -1 if no square can be formed.
     */
    public int maximizeSquareArea(int m, int n, int[] hFences, int[] vFences) {
        int[] hCoords = new int[hFences.length + 2];
        int[] vCoords = new int[vFences.length + 2];

        hCoords[0] = 1;
        hCoords[1] = m;
        System.arraycopy(hFences, 0, hCoords, 2, hFences.length);

        vCoords[0] = 1;
        vCoords[1] = n;
        System.arraycopy(vFences, 0, vCoords, 2, vFences.length);

        Arrays.sort(hCoords);
        Arrays.sort(vCoords);

        Set<Integer> horizontalGaps = new HashSet<>();
        for (int i = 0; i < hCoords.length; i++) {
            for (int j = i + 1; j < hCoords.length; j++) {
                horizontalGaps.add(hCoords[j] - hCoords[i]);
            }
        }

        long maxSide = -1;
        for (int i = 0; i < vCoords.length; i++) {
            for (int j = i + 1; j < vCoords.length; j++) {
                int currentGap = vCoords[j] - vCoords[i];
                if (horizontalGaps.contains(currentGap)) {
                    maxSide = Math.max(maxSide, currentGap);
                }
            }
        }

        if (maxSide == -1) {
            return -1;
        }

        return (int) ((maxSide * maxSide) % 1000000007);
    }
}