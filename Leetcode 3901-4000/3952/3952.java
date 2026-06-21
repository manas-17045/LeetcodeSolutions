// Leetcode 3952: Maximum Total Value of Covered Indices
// https://leetcode.com/problems/maximum-total-value-of-covered-indices/
// Solved on 21st of June, 2026
class Solution {
    /**
     * Calculates the maximum total value of covered indices.
     * 
     * @param nums The array of values.
     * @param s The string indicating covered indices.
     * @return The maximum total value of covered indices.
     */
    public long maxTotal(int[] nums, String s) {
        long totalSum = 0;
        int n = nums.length;
        int i = 0;
        while (i < n) {
            if (s.charAt(i) == '1') {
                int l = i;
                while (i < n && s.charAt(i) == '1') {
                    i++;
                }
                int r = i - 1;
                if (l == 0) {
                    for (int j = 0; j <= r; j++) {
                        totalSum += nums[j];
                    }
                } else {
                    int minVal = nums[l - 1];
                    long blockSum = nums[l - 1];
                    for (int j = l; j <= r; j++) {
                        blockSum += nums[j];
                        if (nums[j] < minVal) {
                            minVal = nums[j];
                        }
                    }
                    totalSum += (blockSum - minVal);
                }
            } else {
                i++;
            }
        }
        return totalSum;
    }
}