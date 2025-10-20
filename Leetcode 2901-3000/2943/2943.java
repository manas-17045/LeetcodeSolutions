// Leetcode 2943: Maximize Area of Square Hole in Grid
// https://leetcode.com/problems/maximize-area-of-square-hole-in-grid/
// Solved on 20th of October, 2025
import java.util.Arrays;

class Solution {
    public int maximizeSquareHoleArea(int n, int m, int[] hBars, int[] vBars) {
        int longestH = longestConsecutive(hBars);
        int longestV = longestConsecutive(vBars);
        int side = Math.min(longestH, longestV) + 1;
        return side * side;
    }

    private int longestConsecutive(int[] arr) {
        if (arr == null || arr.length == 0) return 0;
        Arrays.sort(arr); // in-place
        int best = 1;
        int cur = 1;
        for (int i = 1; i < arr.length; ++i) {
            if (arr[i] == arr[i - 1] + 1) {
                cur++;
            } else {
                if (cur > best) best = cur;
                cur = 1;
            }
        }
        if (cur > best) best = cur;
        return best;
    }
}