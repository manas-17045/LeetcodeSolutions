// Leetcode 3551: Minimum Swaps to Sort by Digit Sum
// https://leetcode.com/problems/minimum-swaps-to-sort-by-digit-sum/
// Solved on 28th of November, 2025
import java.util.Arrays;

class Solution {
    /**
     * Calculates the minimum number of swaps required to sort an array based on a custom comparison logic.
     * The comparison prioritizes digit sum, then the number itself, and finally its original index.
     * @param nums The input array of integers.
     * @return The minimum number of swaps to achieve the sorted order.
     */
    public int minSwaps(int[] nums) {
        int n = nums.length;
        long[] packed = new long[n];
        for (int i = 0; i < n; i++) {
            long digitSum = 0;
            int val = nums[i];
            while (val > 0) {
                digitSum += val % 10;
                val /= 10;
            }
            packed[i] = (digitSum << 50) | ((long) nums[i] << 20) | i;
        }
        Arrays.sort(packed);
        boolean[] visited = new boolean[n];
        int swaps = 0;
        for (int i = 0; i < n; i++) {
            if (visited[i]) {
                continue;
            }
            int cycleSize = 0;
            int current = i;
            while (!visited[current]) {
                visited[current] = true;
                current = (int) (packed[current] & 0xFFFFF);
                cycleSize++;
            }
            if (cycleSize > 1) {
                swaps += cycleSize - 1;
            }
        }
        return swaps;
    }
}