// Leetcode 2274: Maximum Consecutive Floors Without Special Floors
// https://leetcode.com/problems/maximum-consecutive-floors-without-special-floors/
// Solved on 12th of November, 2025
import java.util.Arrays;

class Solution {
    /**
     * Calculates the maximum number of consecutive floors without any special floors.
     *
     * @param bottom The lowest floor number.
     * @param top The highest floor number.
     * @param special An array of floor numbers that are considered special.
     * @return The maximum number of consecutive floors that are not special.
     */
    public int maxConsecutive(int bottom, int top, int[] special) {
        if (special == null || special.length == 0) {
            return top - bottom + 1;
        }
        Arrays.sort(special);
        int maxGap = 0;
        int firstGap = special[0] - bottom;
        if (firstGap > maxGap) {
            maxGap = firstGap;
        }
        for (int i = 1; i < special.length; i++) {
            int gap = special[i] - special[i - 1] - 1;
            if (gap > maxGap) {
                maxGap = gap;
            }
        }
        int lastGap = top - special[special.length - 1];
        if (lastGap > maxGap) {
            maxGap = lastGap;
        }
        return maxGap;
    }
}