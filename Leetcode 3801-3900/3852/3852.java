// Leetcode 3852: Smallest Pair With Different Frequencies
// https://leetcode.com/problems/smallest-pair-with-different-frequencies/
// Solved on 1st of March, 2026
class Solution {
    /**
     * Finds the smallest pair of numbers (x, y) such that x < y and their frequencies in the input array are different.
     * 
     * @param nums An array of integers where 1 <= nums[i] <= 100.
     * @return An array containing the smallest pair [x, y] with different frequencies, or [-1, -1] if no such pair exists.
     */
    public int[] minDistinctFreqPair(int[] nums) {
        int[] freq = new int[101];
        for (int num : nums) {
            freq[num]++;
        }
        
        for (int x = 1; x <= 100; x++) {
            if (freq[x] > 0) {
                for (int y = x + 1; y <= 100; y++) {
                    if (freq[y] > 0 && freq[x] != freq[y]) {
                        return new int[]{x, y};
                    }
                }
            }
        }
        return new int[]{-1, -1};
    }
}