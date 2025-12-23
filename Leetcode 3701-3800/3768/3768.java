// Leetcode 3768: Minimum Inversion Count in Subarrays of Fixed Length
// https://leetcode.com/problems/minimum-inversion-count-in-subarrays-of-fixed-length/
// Solved on 22nd of December, 2025
import java.util.Arrays;

class Solution {
    /**
     * Calculates the minimum inversion count among all subarrays of fixed length k.
     * @param nums The input array of integers.
     * @param k The fixed length of the subarrays.
     * @return The minimum inversion count found.
     */
    public long minInversionCount(int[] nums, int k) {
        int n = nums.length;
        int[] sorted = nums.clone();
        Arrays.sort(sorted);

        int[] unique = new int[n];
        int uniqueCount = 0;
        for (int i = 0; i < n; i++) {
            if (i == 0 || sorted[i] != sorted[i - 1]) {
                unique[uniqueCount++] = sorted[i];
            }
        }

        int[] bit = new int[uniqueCount + 2];
        long currentInv = 0;

        for (int i = 0; i < k; i++) {
            int rank = Arrays.binarySearch(unique, 0, uniqueCount, nums[i]) + 1;
            currentInv += (i - query(bit, rank));
            update(bit, rank, 1);
        }

        long minInv = currentInv;

        for (int i = k; i < n; i++) {
            int outVal = nums[i - k];
            int outRank = Arrays.binarySearch(unique, 0, uniqueCount, outVal) + 1;
            update(bit, outRank, -1);
            currentInv -= query(bit, outRank - 1);

            int inVal = nums[i];
            int inRank = Arrays.binarySearch(unique, 0, uniqueCount, inVal) + 1;
            currentInv += ((k - 1) - query(bit, inRank));
            update(bit, inRank, 1);

            minInv = Math.min(minInv, currentInv);
        }

        return minInv;
    }

    private void update(int[] bit, int index, int delta) {
        while (index < bit.length) {
            bit[index] += delta;
            index += index & -index;
        }
    }

    private int query(int[] bit, int index) {
        int sum = 0;
        while (index > 0) {
            sum += bit[index];
            index -= index & -index;
        }
        return sum;
    }
}