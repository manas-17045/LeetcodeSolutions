// Leetcode 4011: Count Subarrays With Even Odd Ratio I
// https://leetcode.com/problems/count-subarrays-with-even-odd-ratio-i/
// Solved on 3rd of September, 2026
class Solution {
    /**
     * Counts the number of valid subarrays where the ratio of even elements
     * to odd elements is at most a / b and there is at least one odd element.
     *
     * @param nums the input array of integers
     * @param a the numerator of the upper bound ratio
     * @param b the denominator of the upper bound ratio
     * @return the total number of valid subarrays
     */
    public int countRatioSubarrays(int[] nums, int a, int b) {
        int validCount = 0;
        int n = nums.length;

        for (int start = 0; start < n; start++) {
            int evenCount = 0;
            int oddCount = 0;

            for (int end = start; end < n; end++) {
                if ((nums[end] & 1) == 0) {
                    evenCount++;
                } else {
                    oddCount++;
                }

                if (oddCount > 0 && evenCount * b <= oddCount * a) {
                    validCount++;
                }
            }
        }

        return validCount;
    }
}