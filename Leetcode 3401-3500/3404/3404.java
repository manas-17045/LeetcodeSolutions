// Leetcode 3404: Count Special Subsequences
// https://leetcode.com/problems/count-special-subsequences/
// Solved on 4th of December, 2025
import java.util.HashMap;
import java.util.Map;

class Solution {
    /**
     * Counts the number of special subsequences in the given array.
     *
     * @param nums The input array of integers.
     * @return The total count of special subsequences.
     */
    public long numberOfSubsequences(int[] nums) {
        long count = 0;
        int n = nums.length;
        Map<Double, Integer> freq = new HashMap<>();
        for (int r = 4; r < n - 2; r++) {
            int q = r - 2;
            for (int p = 0; p < q - 1; p++) {
                double ratio = (double) nums[p] / nums[q];
                freq.put(ratio, freq.getOrDefault(ratio, 0) + 1);
            }
            for (int s = r + 2; s < n; s++) {
                double ratio = (double) nums[s] / nums[r];
                count += freq.getOrDefault(ratio, 0);
            }
        }
        return count;
    }
}